define(function(require, exports, module) {
  var PluginBase = require("pkg!pluginBase"),
    template = require("tpl!./toolAnnotation"),
    systemMode = require("pkg!systemMode");

  var CanvasSettings = Backbone.Model.extend({
    defaults: {
      strokeStyle: "red",
      lineWidth: 2,
      lineCap: "round",
      lineJoin: "round"
    }
  });
  var canvasSettings = new CanvasSettings();

  var tool = "pen",
    isPaint = false,
    isActive = false,

    stageObjs = [],
    penObjs = [],
    currentObj,

    tempPoint,
    lastPoint,
    nextPoint;
  var View = PluginBase.View.extend({
    id: "toolAnnotation",
    mode: "toolAnnotation",
    template: template,
    initialize: function() {
      this.render();
      this.$input = this.$el.find(".input-text");
      this.$canvas = this.$el.find(".canvas");
      this.stage = new createjs.Stage("canvas");
    },
    obEvents: {
      "system:change.mode": "modeChange"
    },
    modeChange: function(oldMode, newMode) {
      if (newMode !== this.mode && oldMode !== this.mode) {
        return;
      }

      if (newMode === this.mode) {
        return this.show();
      }

      if (oldMode === this.mode) {
        return this.hide();
      }
    },
    show: function() {
      this.$el.addClass("active");
      this.emit("book:disable.action");
    },
    hide: function() {
      this.$el.removeClass("active");
      this.emit("book:enable.action");
    },
    render: function() {
      this.$el.html(this.template()).appendTo($("body"));
    },
    events: {
      "mousedown .canvas": "penDown",
      "mousemove .canvas": "penMove",
      "mouseup .canvas": "penUp",
      "mouseleave .canvas": "penLeave",
      "click .tools": "hideText",
      "blur .input-text": "addText",

      "click .pen,.line,.rectangle,.ellipse,.eraser,.text,.exit": "setTool",
      "click .red,.green,.blue": "setColor",
      "blur .lineWidth": "setWidth"
    },
    penDown: function() {
      if (isActive || tool === "eraser") {
        return;
      }

      currentObj = null;
      this.saveStage(this.stage);

      if (tool === "text") {
        return this.setText(this.getCurPosition(this.stage), canvasSettings);
      }

      isPaint = true;
      lastPoint = this.getCurPosition(this.stage);

      if (tool === "pen") {
        tempPoint = lastPoint;
        penObjs.push(new ShapeExtend("pen", lastPoint, lastPoint));

        this.drawPen(this.stage, penObjs[penObjs.length - 1], lastPoint, lastPoint, canvasSettings);

        this.stage.addChild(penObjs[penObjs.length - 1]);
        this.stage.update();
      }
    },
    penMove: function() {
      var penCount = penObjs.length - 1;

      if (!isPaint || isActive || tool === "eraser") {
        return;
      }
      nextPoint = this.getCurPosition(this.stage);

      if (tool === "pen") {
        this.drawPen(this.stage, penObjs[penCount], tempPoint, nextPoint, canvasSettings);

        penObjs[penCount].lastPoint = this.getNewPenPosition(penObjs[penCount], nextPoint).lastPoint;
        penObjs[penCount].nextPoint = this.getNewPenPosition(penObjs[penCount], nextPoint).nextPoint;
      } else {
        this.restoreStage(this.stage);
        var pic = this.drawPic(this.stage, tool, lastPoint, nextPoint, canvasSettings);
        pic.name = "tempObj";
      }

      tempPoint = nextPoint;
    },
    penUp: function() {
      if (!isPaint || isActive || tool === "eraser") {
        return;
      }

      isPaint = false;

      if (tool === "pen") {
        this.addPicEvents(this.stage, penObjs[penObjs.length - 1]);
      }

      this.saveStage(this.stage);
    },
    penLeave: function() {
      isPaint = false;
    },
    getNewPenPosition: function(penObj, point) {
      var lastPointLocal = this.getPoint(penObj.lastPoint),
        nextPointLocal = this.getPoint(penObj.nextPoint);

      lastPointLocal.x = lastPointLocal.x > point.x ? point.x: lastPointLocal.x;
      lastPointLocal.y = lastPointLocal.y > point.y ? point.y: lastPointLocal.y;
      nextPointLocal.x = nextPointLocal.x < point.x ? point.x: nextPointLocal.x;
      nextPointLocal.y = nextPointLocal.y < point.y ? point.y: nextPointLocal.y;

      return {
        lastPoint: lastPointLocal,
        nextPoint: nextPointLocal
      };
    },
    getPoint: function(point) {
      return {
        x: point.x,
        y: point.y
      };
    },
    getCurPosition: function(stage) {
      return {
        x: stage.mouseX,
        y: stage.mouseY
      };
    },
    addText: function() {
      if (this.$input[0].value === "" && isActive) {
        return this.setText({
          x: this.stage.mouseX,
          y: this.stage.mouseY
        }, canvasSettings);
      } else if (this.$input[0].value === "" && !isActive) {
        return this.hideText();
      }

      this.drawText(this.stage, this.getTextAttrs().position, this.getTextAttrs().textStyle);
      this.hideText();
    },
    setText: function(position, canvasSettings) {
      isActive = true;
      var txtAttrs = this.createTextAttrs(position, canvasSettings);

      this.$input.show();
      this.$input[0].style.border = txtAttrs.border;
      this.$input[0].style.fontFamily = txtAttrs.fontFamily;
      this.$input[0].style.color = txtAttrs.color;
      this.$input[0].style.fontSize = txtAttrs.fontSize;
      this.$input[0].style.fontWeight = txtAttrs.fontWeight;
      this.$input[0].style.height = txtAttrs.height;
      this.$input[0].style.width = txtAttrs.width;
      this.$input[0].style.position = txtAttrs.position;
      this.$input[0].style.left = txtAttrs.left;
      this.$input[0].style.top = txtAttrs.top;
    },
    hideText: function() {
      isActive = false;
      this.$input[0].value = "";
      this.$input.hide();
    },
    createTextAttrs: function(position, canvasSettings) {
      var fontSize = canvasSettings.get("lineWidth") + 11,
        height = fontSize + 4,
        width = height * 5,
        canvasLeft = this.$canvas.offset().left,
        canvasTop = this.$canvas.offset().top,
        textLeft = canvasLeft + position.x,
        textTop = canvasTop + position.y - this.$input.height() / 2;

      if (textLeft < canvasLeft) {
        textLeft = canvasLeft;
      }
      if (textTop < canvasTop) {
        textTop = canvasTop;
      }
      if (textLeft + width > canvasLeft + this.$canvas.width()) {
        textLeft = canvasLeft + this.$canvas.width() - width;
      }
      if (textTop + height > canvasTop + this.$canvas.height()) {
        textTop = canvasTop + this.$canvas.height() - height;
      }

      return {
        border: "1px solid #f60",
        color: canvasSettings.get("strokeStyle"),
        fontFamily: "arial",
        fontSize: fontSize,
        fontWeight: "bold",
        height: height,
        width: width,
        position: "absolute",
        left: textLeft - 218,
        top: textTop - 22
      };
    },
    getTextAttrs: function() {
      var fontSize = this.$input[0].style.fontSize.substring(0, this.$input[0].style.fontSize.indexOf("px"));

      return {
        position: {
          x: this.$input.offset().left - this.$canvas.offset().left,
          y: this.$input.offset().top - this.$canvas.offset().top
        },
        textStyle: {
          text: this.$input[0].value,
          color: this.$input[0].style.color,
          fontWeight: "bold",
          fontSize: fontSize,
          fontFamily: "arial"
        }
      };
    },
    drawPic: function(stage, tool, lastPoint, nextPoint, canvasSettings) {
      switch (tool) {
      case "line":
        return this.drawLine(stage, lastPoint, nextPoint, canvasSettings);
      case "rectangle":
        return this.drawRectangle(stage, lastPoint, nextPoint, canvasSettings);
      case "ellipse":
        return this.drawEllipse(stage, lastPoint, nextPoint, canvasSettings);
      default:
        break;
      }
    },
    drawPen: function(stage, pen, lastPoint, nextPoint, canvasSettings) {
      pen.graphics.beginStroke(canvasSettings.get("strokeStyle"))
                  .beginFill(canvasSettings.get("strokeStyle"))
                  .setStrokeStyle(canvasSettings.get("lineWidth"), canvasSettings.get("lineCap"))
                  .moveTo(lastPoint.x, lastPoint.y).lineTo(nextPoint.x, nextPoint.y);
      stage.update();

      return pen;
    },
    drawText: function(stage, position, textStyle) {
      var text = new TextExtend("text"),
      hitArea = new ShapeExtend();

      text.text = textStyle.text;
      text.color = textStyle.color;
      text.fontWeight = textStyle.fontWeight;
      text.fontSize = textStyle.fontSize;
      text.fontFamily = textStyle.fontFamily;
      text.font = text.fontWeight + " " + text.fontSize + "px " + text.fontFamily;
      text.x = position.x;
      text.y = position.y;

      text.lastPoint = this.getPoint({
        x: text.x,
        y: text.y
      });
      text.nextPoint = this.getPoint({
        x: text.x + text.getMeasuredWidth(),
        y: text.y + text.getMeasuredHeight()
      });

      hitArea.graphics.beginFill("#000")
                      .drawRect(0, 0, text.getMeasuredWidth(), text.getMeasuredHeight());
      text.hitArea = hitArea;

      this.addPicEvents(stage, text);
      stage.addChild(text);
      stage.update();

      return text;
    },
    drawLine: function(stage, lastPoint, nextPoint, canvasSettings) {
      var line = new ShapeExtend("line", lastPoint, nextPoint);
      line.graphics.beginStroke(canvasSettings.get("strokeStyle"))
                   .setStrokeStyle(canvasSettings.get("lineWidth"), canvasSettings.get("lineCap"))
                   .moveTo(lastPoint.x, lastPoint.y).lineTo(nextPoint.x, nextPoint.y);

      this.addPicEvents(stage, line);
      stage.addChild(line);
      stage.update();

      return line;
    },
    drawRectangle: function(stage, lastPoint, nextPoint, canvasSettings) {
      var position = this.getPicPosition(lastPoint, nextPoint),
      rectangle = new ShapeExtend("rectangle", lastPoint, nextPoint);
      rectangle.graphics.beginStroke(canvasSettings.get("strokeStyle"))
                        .setStrokeStyle(canvasSettings.get("lineWidth"), canvasSettings.get("lineCap"), canvasSettings.get("lineJoin"))
                        .drawRect(position.x, position.y, Math.abs(lastPoint.x - nextPoint.x), Math.abs(lastPoint.y - nextPoint.y));

      this.addPicEvents(stage, rectangle);
      stage.addChild(rectangle);
      stage.update();

      return rectangle;
    },
    drawEllipse: function(stage, lastPoint, nextPoint, canvasSettings) {
      var position = this.getPicPosition(lastPoint, nextPoint),
      ellipse = new ShapeExtend("ellipse", lastPoint, nextPoint);
      ellipse.graphics.beginStroke(canvasSettings.get("strokeStyle"))
                      .setStrokeStyle(canvasSettings.get("lineWidth"), canvasSettings.get("lineCap"), canvasSettings.get("lineJoin"))
                      .drawEllipse(position.x, position.y, Math.abs(lastPoint.x - nextPoint.x), Math.abs(lastPoint.y - nextPoint.y));

      this.addPicEvents(stage, ellipse);
      stage.addChild(ellipse);
      stage.update();

      return ellipse;
    },
    getPicPosition: function(lastPoint, nextPoint) {
      var position = {
        x: null,
        y: null
      };

      if ((lastPoint.x <= nextPoint.x) && (lastPoint.y <= nextPoint.y)) {
        position = this.getPoint(lastPoint);
      } else if ((lastPoint.x <= nextPoint.x) && (lastPoint.y >= nextPoint.y)) {
        position = this.getPoint({
          x: lastPoint.x,
          y: nextPoint.y
        });
      } else if ((lastPoint.x >= nextPoint.x) && (lastPoint.y <= nextPoint.y)) {
        position = this.getPoint({
          x: nextPoint.x,
          y: lastPoint.y
        });
      } else if ((lastPoint.x >= nextPoint.x) && (lastPoint.y >= nextPoint.y)) {
        position = this.getPoint({
          x: nextPoint.x,
          y: nextPoint.y
        });
      }

      return position;
    },
    addPicEvents: function(stage, Obj) {
      var that = this;

      Obj.addEventListener("mousedown",
      function(event) {
        if (tool === "eraser") {
          stage.removeChild(Obj);
          that.saveStage(stage);
          return;
        }

        isActive = false; //激活Pic时，使text输入框消失
        that.$input.blur();

        isActive = true;
        currentObj = Obj;
        that.addAnchors(that, stage, event.target);
        tempPoint = {
          x: event.stageX,
          y: event.stageY
        }; //记录鼠标移动的上一个point            
        var offset = {
          x: event.target.x - event.stageX,
          y: event.target.y - event.stageY
        }; //Pic对象在移动过程中的偏移量  

        event.addEventListener("mousemove",
        function(evt) { //图形移动事件                
          evt.target.x = evt.stageX + offset.x;
          evt.target.y = evt.stageY + offset.y;
          //图形移动时，改变Pic对象的坐标点
          evt.target.lastPoint.x += evt.stageX - tempPoint.x;
          evt.target.lastPoint.y += evt.stageY - tempPoint.y;
          evt.target.nextPoint.x += evt.stageX - tempPoint.x;
          evt.target.nextPoint.y += evt.stageY - tempPoint.y;
          //实时地添加指示点 
          that.addAnchors(that, stage, event.target);
          tempPoint = {
            x: evt.stageX,
            y: evt.stageY
          };
        });

        event.addEventListener("mouseup",
        function() { //鼠标放开，Pic激活状态消失
          isActive = false;
        });
      });
    },
    addAnchors: function(that, stage, Obj) {
      var anchors = that.getAnchors(that, Obj);

      that.removeAnchors(stage);
      that.addAnchorsEvents(that, stage, anchors, Obj);
      that.addAnchorsToStage(stage, anchors, Obj.picType);
    },
    getAnchors: function(that, Obj) {
      var anchors = [];

      anchors.push(that.getAnchor("lt_anchor", Obj));
      anchors.push(that.getAnchor("lb_anchor", Obj));
      anchors.push(that.getAnchor("rt_anchor", Obj));
      anchors.push(that.getAnchor("rb_anchor", Obj));

      return anchors;
    },
    getAnchor: function(name, Obj) {
      var strokeStyle = createjs.Graphics.getRGB(30, 156, 217),
        r_Anchor,
        anchor = new ShapeExtend();

      if (Obj.picType === "text") {
        r_Anchor = 5;
      } else {
        r_Anchor = Obj.graphics._strokeStyleInstructions[0].params[1] / 2 + 5;
      }

      anchor.name = name;
      switch (name) {
        case "lt_anchor":
          if (Obj.picType === "text") {
            anchor.lastPoint = {
              x: Obj.x,
              y: Obj.y
            };
            break;
          }
          anchor.lastPoint = Obj.lastPoint;
          break;
        case "lb_anchor":
          if (Obj.picType === "text") {
            anchor.lastPoint = {
              x: Obj.x,
              y: Obj.y + Obj.getMeasuredHeight()
            };
            break;
          }
          anchor.lastPoint = {
            x: Obj.lastPoint.x,
            y: Obj.nextPoint.y
          };
          break;
        case "rt_anchor":
          if (Obj.picType === "text") {
            anchor.lastPoint = {
              x: Obj.x + Obj.getMeasuredWidth(),
              y: Obj.y
            };
            break;
          }
          anchor.lastPoint = {
            x: Obj.nextPoint.x,
            y: Obj.lastPoint.y
          };
          break;
        case "rb_anchor":
          if (Obj.picType === "text") {
            anchor.lastPoint = {
              x: Obj.x + Obj.getMeasuredWidth(),
              y: Obj.y + Obj.getMeasuredHeight()
            };
            break;
          }
          anchor.lastPoint = Obj.nextPoint;
          break;
        default:
          break;
      }
      anchor.graphics.beginStroke(strokeStyle)
            .beginFill(strokeStyle)
            .drawCircle(anchor.lastPoint.x, anchor.lastPoint.y, r_Anchor);

      return anchor;
    },
    addAnchorsEvents: function(that, stage, anchors, Obj) {
      if (Obj.picType === "pen") {
        return that.removeAnchors(stage);
      }

      var i, anchor;

      for (i in anchors) {
        anchor = anchors[i];

        anchor.addEventListener("mousedown",
        function(event) {
          isActive = true;
          currentObj = Obj;

          tempPoint = {
            x: event.stageX,
            y: event.stageY
          };
          var offset = {
            x: event.target.x - event.stageX,
            y: event.target.y - event.stageY
          };

          event.addEventListener("mousemove",
          function(evt) {
            var offsetPic = {
              x: evt.stageX - tempPoint.x,
              y: evt.stageY - tempPoint.y
            };
            stage.removeChild(Obj);
            Obj.name = "tempObj";
            that.restoreStage(stage);

            Obj = that.updatePicPoints(evt.target.name, Obj, offsetPic);
            Obj = that.reDrawPic(stage, Obj);
            Obj.name = "tempObj";
            that.addAnchors(that, stage, Obj); // 重新构造“指示点”
            anchors = that.getAnchors(that, Obj);
            that.addAnchorsEvents(that, stage, anchors, Obj);

            evt.target.x = evt.stageX + offset.x; //“指示点”偏移过程
            evt.target.y = evt.stageY + offset.y;
            tempPoint = {
              x: evt.stageX,
              y: evt.stageY
            }; //保存移动前一个point
            currentObj = Obj; //调整图形后，保存当前激活对象为调整后的对象
          });

          event.addEventListener("mouseup",
          function() {
            isActive = false;
            that.saveStage(stage);
            that.addAnchorsToStage(stage, anchors, Obj.picType);
          });
        });
      }
    },
    addAnchorsToStage: function(stage, anchors, picType) { //添加“指示点”到stage
      if (picType === "line") {
        stage.addChild(anchors[0], anchors[3]);
      } else {
        stage.addChild(anchors[0], anchors[1], anchors[2], anchors[3]);
      }

      stage.update();
    },
    updatePicPoints: function(anchorType, Obj, offset) { //根据指示点的name，分别作更新图形的坐标信息的处理
      switch (anchorType) {
      case "lt_anchor":
        if (Obj.picType === "text") {
          Obj.x += offset.x;
          Obj.y += offset.y;
          Obj.fontSize *= 1 - offset.y / Obj.getMeasuredHeight();
        } else {
          Obj.lastPoint.x += offset.x;
          Obj.lastPoint.y += offset.y;
        }
        break;
      case "lb_anchor":
        if (Obj.picType === "text") {
          Obj.x += offset.x;
          Obj.fontSize *= 1 + offset.y / Obj.getMeasuredHeight();
        } else {
          Obj.lastPoint.x += offset.x;
          Obj.nextPoint.y += offset.y;
        }
        break;
      case "rt_anchor":
        if (Obj.picType === "text") {
          Obj.y += offset.y;
          Obj.fontSize *= 1 - offset.y / Obj.getMeasuredHeight();
        } else {
          Obj.lastPoint.y += offset.y;
          Obj.nextPoint.x += offset.x;
        }
        break;
      case "rb_anchor":
        if (Obj.picType === "text") {
          Obj.fontSize *= 1 + offset.y / Obj.getMeasuredHeight();
        } else {
          Obj.nextPoint.x += offset.x;
          Obj.nextPoint.y += offset.y;
        }
        break;
      default:
        break;
      }

      if (Obj.picType === "text") {
        if (Obj.fontSize < 12) {
          Obj.fontSize = 12;
        }
      }

      return Obj;
    },
    reDrawPic: function(stage, obj) { //调整图形时,调用图形之前的属性重绘并调整大小
      var canvasSettingsLocal, textStyle;

      if (obj.picType !== "text") {
        canvasSettingsLocal = new CanvasSettings({
          strokeStyle: obj.graphics._strokeInstructions[0].params[1],
          lineWidth: obj.graphics._strokeStyleInstructions[0].params[1],
          lineCap: obj.graphics._strokeStyleInstructions[1].params[1],
          lineJoin: obj.graphics._strokeStyleInstructions[2].params[1]
        });
      }

      switch (obj.picType) {
      case "line":
        return this.drawLine(stage, obj.lastPoint, obj.nextPoint, canvasSettingsLocal);
      case "rectangle":
        return this.drawRectangle(stage, obj.lastPoint, obj.nextPoint, canvasSettingsLocal);
      case "ellipse":
        return this.drawEllipse(stage, obj.lastPoint, obj.nextPoint, canvasSettingsLocal);
      case "text":
        textStyle = {
          text: obj.text,
          color: obj.color,
          fontWeight: obj.fontWeight,
          fontSize: obj.fontSize,
          fontFamily: obj.fontFamily
        };
        return this.drawText(stage, {
          x: obj.x,
          y: obj.y
        },
        textStyle);
      default:
        break;
      }
    },
    removeAnchors: function(stage) {
      stage.removeChild(stage.getChildByName("lt_anchor"));
      stage.removeChild(stage.getChildByName("lb_anchor"));
      stage.removeChild(stage.getChildByName("rt_anchor"));
      stage.removeChild(stage.getChildByName("rb_anchor"));

      stage.update();
    },
    saveStage: function(stage) {
      stageObjs = [];
      this.removeAnchors(stage);

      var i;
      for (i = 0; i < stage.getNumChildren(); i++) {
        var child = stage.getChildAt(i);
        child.name = "normalObj";
        stageObjs.push(child);
      }

      stage.update();
    },
    restoreStage: function(stage) {
      this.removeAnchors(stage);
      stage.removeChild(stage.getChildByName("tempObj"));

      var i;
      for (i in stageObjs) {
        stage.addChild(stageObjs[i]);
      }
      stage.update();
      stageObjs = [];
    },
    setTool: function(evt) {
      if (evt.target.className === "exit") {
        return this.hide();
      }

      tool = evt.target.className;
      $("." + tool).siblings(".current").removeClass("current");
      $("." + tool).addClass("current");
    },
    setWidth: function(evt) {
      var eNum = parseFloat(evt.target.value);

      if (isNaN(eNum)) {
        alert("请输入数字类型！");
        evt.target.value = "";
        return;
      } else if (eNum < 1 || eNum > 50) {
        alert("请输入范围内的数字！");
        evt.target.value = "";
        return;
      } else {
        canvasSettings.set({
          lineWidth: eNum
        });
      }
    },
    setColor: function(evt) {
      if (currentObj) {
        this.changePicColor(this.stage, currentObj, evt.target.className);
      } else {
        canvasSettings.set({
          strokeStyle: evt.target.className
        });
      }
    },
    changePicColor: function(stage, currentObj, color) { //???改变激活状态的color
      if (currentObj.picType === "text") { //说明改变的是text
        currentObj.color = color;
        stage.update();
        return;
      } else {
        currentObj.graphics._strokeInstructions[0].params[1] = color;

        if (currentObj.picType === "pen") {
          this.changePenColor(stage, currentObj, color);
        }
      }

      stage.update();
    },
    changePenColor: function(stage, currentObj, color) {
      var points = [],
        c,
        i,
        j,
        graphics = new createjs.Graphics();

      if (currentObj.graphics._activeInstructions.length !== 2) {
        for (c in currentObj.graphics._activeInstructions) {
          points.push({
            x: currentObj.graphics._activeInstructions[c].params[0],
            y: currentObj.graphics._activeInstructions[c].params[1]
          });
        }
        graphics.beginStroke(color)
                .beginFill(color)
                .setStrokeStyle(currentObj.graphics._strokeStyleInstructions[0].params[1], currentObj.graphics._strokeStyleInstructions[1].params[1], currentObj.graphics._strokeStyleInstructions[2].params[1]);

        for (i = 0, j = 1; j < points.length; i++, j++) {
          if (graphics._activeInstructions.length > 151552) {
            return;
          }
          graphics.mt(points[i].x, points[i].y).lt(points[j].x, points[j].y);
        }
        currentObj.graphics._activeInstructions = graphics._activeInstructions;
      } else {
        for (c in currentObj.graphics._instructions) {
          points.push({
            x: currentObj.graphics._instructions[c].params[0],
            y: currentObj.graphics._instructions[c].params[1]
          });
        }

        graphics.beginStroke(color)
                .beginFill(color)
                .setStrokeStyle(currentObj.graphics._strokeStyleInstructions[0].params[1], currentObj.graphics._strokeStyleInstructions[1].params[1], currentObj.graphics._strokeStyleInstructions[2].params[1]);

        for (i = 1, j = 2; j < points.length - 1; i += 11, j += 11) {
          graphics.mt(points[i].x, points[i].y).lt(points[i + 1].x, points[i + 1].y);
        }
        currentObj.graphics = graphics;
      }
    }
  });
  return View;
});