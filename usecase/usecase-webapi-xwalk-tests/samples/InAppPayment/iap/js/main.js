/*
Copyright (c) 2014 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Liu,Yun <yunx.liu@intel.com>

*/

window.onload = function() {
  if (typeof iap == "undefined") {
    document.getElementById("datawindow").innerHTML = 'No IAP support<br>' + 'Test Fail';
    return;
  }

  var testFlag = {
      green: false,
      red: false
  };
  var key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsEVjLWKJ5B7EKjnH5NVx4eh83xntg1WXFIQhLXgtmiCU0Ro27dN8Q7Q5HIif4ugkFcQWFhlDC/WsliDKtLZQkadmS1sUweOanIo5+ZbNaQ1ITWwtkNdnPb+tRJCjhngft1hFIfLGsKrBMxS8slaWaQ537wgex74Pv5mxuQLhsFyei5GffzDQDz4KN6sQHPqtB+GLDWqKKk2bdAiopQRFRUwYR8edAYcHiMHHZSfidOjaYD1/timhFIUnwFihtvNy4K7OStjoy6kEwCmX9/zXS3SxKkOfk2bNg/Edc8xgym8GkfObUliySSNxS9ukzp1ShDuSjdwfJVt5mvmXk+7jiQIDAQAB';
  iap.init(key);

  var status = function() {
    if (testFlag.green && testFlag.red) {
      document.getElementById("datawindow").innerHTML = "Test Pass<br>" + document.getElementById("datawindow").innerHTML;
    }
  }

  var errorCallBack = function(error) {
    document.getElementById("datawindow").innerHTML = "Test Fail<br> Error: " + error;
  }

  var queryProductsCallBack = function(products) {
    testFlag.green = true;
    if (products.length == 0) {
        document.getElementById("datawindow").innerHTML = "No product available";
        return;
    }

    document.getElementById("datawindow").innerHTML = "";
    for (var i=0; i<products.length; i++) {
      var f1 = "ID: " + products[i]["productId"] + "<br>";
      var f2 = "Price: " + products[i]["price"] + "<br>";
      var f3 = "Currency: " + products[i]["price_currency_code"] + "<br>";
      var f4 = "Title: " + products[i]["title"] + "<br>";
      var f5 = "Description: " + products[i]["description"] + "<br>----------<br>"
      document.getElementById("datawindow").innerHTML += f1 + f2 + f3 + f4 + f5;
    }
    status();
  }

  var buyCallBack = function(result) {
    testFlag.green = true;
    var orderId = result.orderId;
    var packageName = result.packageName;
    var productId = result.productId;
    var purchaseTime = result.purchaseTime;
    var purchaseState = result.purchaseState;

    var m = new Date(1970,0,1);
    m.setSeconds(purchaseTime/1000);
    var dateStringGMT =
      m.getUTCFullYear() +"/"+
      ("0" + (m.getUTCMonth()+1)).slice(-2) +"/"+
      ("0" + m.getUTCDate()).slice(-2) + " " +
      ("0" + m.getUTCHours()).slice(-2) + ":" +
      ("0" + m.getUTCMinutes()).slice(-2) + ":" +
      ("0" + m.getUTCSeconds()).slice(-2);

    document.getElementById("datawindow").innerHTML += "Buy returned:"
      + "<br>Order ID: " + orderId
      + "<br>Package Name: " + packageName
      + "<br>Product ID: " + productId
      + "<br>Purchase Time(GMT): " + dateStringGMT
      + "<br>Purchase State: " + purchaseState + "<br>";
    status();
  }

  document.getElementById("btnQuery").onclick = function() {
    iap.queryProductDetails(["gas", "yearly", "premium"]).then(queryProductsCallBack, errorCallBack);
  }

  document.getElementById("btnBuy").onclick = function() {
    iap.buy("gas").then(buyCallBack, errorCallBack);
  }
}
