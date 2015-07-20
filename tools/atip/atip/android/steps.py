# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Yang, Yunlong <yunlongx.yang@intel.com>

import android
import sys
from behave import step
reload(sys)
sys.setdefaultencoding('utf-8')


# @step(u'launch "{app_name}" on android')
# def launch_app_by_name(context, app_name):
#     android.launch_app_by_name(context, app_name)

@step(u'I launch "{app_name}" with "{apk_pkg_name}" and "{apk_activity_name}" on android')
def launch_app_by_names(context, app_name, apk_pkg_name, apk_activity_name):
    android.launch_app_by_name(
        context,
        app_name,
        apk_pkg_name,
        apk_activity_name)


@step(u'I turn on device')
def wake_up(context):
	context.android.turnOnDevice()


@step(u'I turn off device')
def wake_up(context):
	context.android.turnOffDevice()	

# The possible orientation is:
# natural or n
# left or l
# right or r
# upsidedown or u (notes: "upsidedown" can not be set until Android 4.3.)
@step(u'I set orientation "{orientation}"')
def set_orientation(context, orientation):
	context.android.setDeviceOrientation(orientation)


# take screenshot and save to local file "home.png", can not work until Android 4.2.
@step(u'I take screenshot as "{name}"')
def take_screenshot(context, name):
	context.android.takeScreenshot(name)


# open notification, can not work until Android 4.3.
@step(u'I open notification')
def open_notification(context):
	assert context.android.openNotification()


# open quick settings, can not work until Android 4.3.
@step(u'I open quick settings')
def open_quick_settings(context):
	assert context.android.openQuickSettings()

# frequently-used key: home, back, left, right, up, down, center, menu, search, enter, 
# delete(or del), recent(recent apps), volume_up, volume_down, volume_mute, camera, power
@step(u'I press "{key}" on android')
def press_key(context, key):
	context.android.pressKeyBy(key)


@step(u'I force to run all watchers')
def force_run_watchers(context):
	context.android.runAllWatchers()


@step(u'I remove all watchers')
def clear_all_watchers(context):
	context.android.removeAllWatchers()


@step(u'I register watcher "{watcher_name}" when "{when_text}" click "{click_text}"')
def register_watcher_when(context, watcher_name, when_text, click_text):
	context.android.registerWatcher(watcher_name, when_text, click_text)


@step(u'I register watcher2 "{watcher_name}" when "{when_text1}" and "{when_text2}" click "{click_text}"')
def register_watcher_when2(context, watcher_name, when_text1, when_text2, click_text):
	context.android.registerWatcher(watcher_name, when_text1, click_text, when_text2)


@step(u'I should see text "{text_name}"')
def select_text_object(context, text_name):
	assert context.android.selectTvObjectBy(text_name).exists


@step(u'I should see image "{image_name}"')
def select_image_object(context, image_name):
	assert context.android.selectImageViewObjectBy(image_name).exists	


@step(u'I should see web "{web_desc}"')
def select_web_object(context, web_desc):
	assert context.android.selectWebObjectBy(web_desc).exists


@step(u'I should see view "{view_desc}"')
def select_view_object(context, view_desc):
	assert context.android.selectViewObjectBy(view_desc).exists


@step(u'I should see class "{class_name}" on the "{relative}" side of text "{text_name}"')
def select_relative_text_object(context, class_name, relative, text_name):
	ob = context.android.selectTvObjectBy(text_name)
	assert ob.exists
	assert context.android.selectRelativeObjectBy(ob, relative, class_name).exists


@step(u'I should see class "{class_name}" on the "{relative}" side of view "{view_desc}"')
def select_relative_view_object(context, class_name, relative, view_desc):
	ob = context.android.selectViewObjectBy(view_desc)
	assert ob.exists
	assert context.android.selectRelativeObjectBy(ob, relative, class_name).exists	


@step(u'I should see class "{class_target}" on the "{relative}" side of any "{class_name}" "{value_name}"')
def select_relative_any_object(context, class_target, relative, class_name, view_desc):
	ob = context.android.selectAnyObjectBy(value_name, class_name)
	assert ob.exists
	assert context.android.selectRelativeObjectBy(ob, relative, class_target).exists		


@step(u'I click button "{button_name}"')
def click_button_object(context, button_name):
	ob = context.android.selectBtnObjectBy(button_name)
	if ob.exists:
		assert context.android.clickBtnObject(ob)
	else:
		ob = context.android.selectImageBtnObjectBy(button_name)
		assert ob.exists
		assert context.android.clickBtnObject(ob)


@step(u'I click other "{class_name}" by "{which_key}" "{which_value}"')
def click_other_view(context, class_name, which_key, which_value):
	ob = context.android.selcetObjectBy(which_key, which_value, class_name)
	assert ob.exists
	assert context.android.clickBtnObject(ob)


@step(u'I click object "{key}"')
def click_any_object(context, key):
	ob = context.android.get2InfoTemp(key)
	assert ob.exists
	assert context.android.clickBtnObject(ob)


@step(u'I edit text "{edit_text}" to input "{text}"')
def set_edittext_object(context, edit_text, text):
	ob = context.android.selectEdtObjectBy(edit_text)
	assert ob.exists
	assert context.android.setEditText(ob, text)


@step(u'I edit index {n:d} text to input "{text}"')
def set_index_edittext_object(context, n, text):
	ob = context.android.selectEdtObjectBy("")[n]
	assert ob.exists
	assert context.android.setEditText(ob, text)


@step(u'I compare text "{text_name}" info "{what}" with "{except_result}"')
def compare_text_with_result(context, text_name, what, except_result):
	ob = context.android.selectTvObjectBy(text_name)
	assert ob.exists
	if context.android.getObjectInfo(ob, what) == except_result:
		assert True
	else:
		assert False


@step(u'I compare view "{view_desc}" info "{what}" with "{except_result}"')
def compare_view_with_result(context, view_desc, what, except_result):
	ob = context.android.selectViewObjectBy(view_desc)
	assert ob.exists
	if context.android.getObjectInfo(ob, what) == except_result:
		assert True
	else:
		assert False


@step(u'I save text object "{text_name}" to temporary value "{key}"')
def save_text_info_temp(context, text_name, key):
	ob = context.android.selectTvObjectBy(text_name)
	assert ob.exists
	assert context.android.save2InfoTemp(ob, key)


@step(u'I save view object "{view_desc}" to temporary value "{key}"')
def save_view_info_temp(context, view_desc, key):
	ob = context.android.selectViewObjectBy(view_desc)
	assert ob.exists
	assert context.android.save2InfoTemp(ob, key)


@step(u'I save any object "{class_name}" "{value_name}" to temporary value "{key}"')
def save_any_info_temp(context, class_name, value_name, key):
	ob = context.android.selectAnyObjectBy(value_name, class_name)
	assert ob.exists
	assert context.android.save2InfoTemp(ob, key)	


@step(u'I save "{class_name}" on the "{relative}" side of text "{text_name}" to temporary value "{key}"')
def save_relative_text_object(context, class_name, relative, text_name, key):
	ob = context.android.selectTvObjectBy(text_name)
	assert ob.exists
	relative_ob = context.android.selectRelativeObjectBy(ob, relative, class_name)
	assert relative_ob.exists
	assert context.android.save2InfoTemp(relative_ob, key)


@step(u'I save "{class_name}" on the "{relative}" side of view "{view_desc}" to temporary value "{key}"')
def save_relative_view_object(context, class_name, relative, view_desc, key):
	ob = context.android.selectViewObjectBy(view_desc)
	assert ob.exists
	relative_ob = context.android.selectRelativeObjectBy(ob, relative, class_name)
	assert relative_ob.exists
	assert context.android.save2InfoTemp(relative_ob, key)


@step(u'I save "{class_target}" on the "{relative}" side of any "{class_name}" "{value_name}" to temporary value "{key}"')
def save_relative_any_object(context, class_target, relative, class_name, value_name, key):
	ob = context.android.selectAnyObjectBy(value_name, class_name)
	assert ob.exists
	relative_ob = context.android.selectRelativeObjectBy(ob, relative, class_target)
	assert relative_ob.exists
	assert context.android.save2InfoTemp(relative_ob, key)	


@step(u'I compare object "{key1}" equal "{key2}" on info "{what}"')
def equal_with_keys(context, key1, key2, what):
	ob1 = context.android.get2InfoTemp(key1)
	ob2 = context.android.get2InfoTemp(key2)
	if context.android.getObjectInfo(ob1, what) == context.android.getObjectInfo(ob2, what):
		assert True
	else:
		assert False


@step(u'I compare object "{key1}" unequal "{key2}" on info "{what}"')
def unequal_with_keys(context, key1, key2, what):
	ob1 = context.android.get2InfoTemp(key1)
	ob2 = context.android.get2InfoTemp(key2)
	if context.android.getObjectInfo(ob1, what) != context.android.getObjectInfo(ob2, what):
		assert True
	else:
		assert False


@step(u'I scroll to end')
def scroll_to_end(context):
	assert context.android.scrollToEnd()


@step(u'I fling "{orientation}" goto "{direction}"')
def fling_by(context, orientation, direction):
	assert context.android.flingBy(orientation, direction)


@step(u'I swipe object "{key}" to "{orientation}"')
def swipe_to(context, key, orientation):
	ob = context.android.get2InfoTemp(key)
	assert ob.exists
	assert context.android.swipeTo(ob, orientation)


@step(u'I process text object "{text_name}"')
def process_text_info_temp(context, text_name=""):
	context.android.process_args['func_name'] = process_text_info_temp
	if text_name:
		context.android.process_args["func_args"] = [text_name, ]
	else:
		text_name = context.android.process_args["func_args"]
	def save_process():	
		ob = context.android.selectTvObjectBy(text_name)
		assert ob.exists
		return ob
	return save_process


@step(u'I process view object "{view_desc}"')
def process_view_info_temp(context, view_desc=""):
	context.android.process_args['func_name'] = process_view_info_temp
	if view_desc:
		context.android.process_args["func_args"] = [view_desc, ]
	else:
		view_desc = context.android.process_args["func_args"]
	def save_process():	
		ob = context.android.selectViewObjectBy(view_desc)
		assert ob.exists
		return ob
	return save_process


@step(u'I process any object "{class_name}" "{value_name}"')
def process_any_info_temp(context, class_name="", value_name=""):
	context.android.process_args['func_name'] = process_any_info_temp
	if class_name and value_name:
		context.android.process_args["func_args"] = [class_name, value_name]
	else:
		class_name, value_name = context.android.process_args["func_args"]
	def save_process():	
		ob = context.android.selectAnyObjectBy(value_name, class_name)
		assert ob.exists
		return ob
	return save_process	


@step(u'I process "{class_name}" on the "{relative}" side of text "{text_name}"')
def process_relative_text_object(context, class_name="", relative="", text_name=""):
	context.android.process_args['func_name'] = process_relative_text_object
	if class_name and relative and text_name:
		context.android.process_args["func_args"] = [class_name, relative, text_name]
	else:
		class_name, relative, text_name = context.android.process_args["func_args"]
	def save_process():
		ob = context.android.selectTvObjectBy(text_name)
		assert ob.exists
		relative_ob = context.android.selectRelativeObjectBy(ob, relative, class_name)
		assert relative_ob.exists	
		return relative_ob
	return save_process


@step(u'I process "{class_name}" on the "{relative}" side of view "{view_desc}"')
def process_relative_view_object(context, class_name="", relative="", view_desc=""):
	context.android.process_args['func_name'] = process_relative_view_object
	if class_name and relative and view_desc:
		context.android.process_args["func_args"] = [class_name, relative, view_desc]
	else:
		class_name, relative, view_desc = context.android.process_args["func_args"]
	def save_process():
		ob = context.android.selectViewObjectBy(view_desc)
		assert ob.exists
		relative_ob = context.android.selectRelativeObjectBy(ob, relative, class_name)
		assert relative_ob.exists	
		return relative_ob
	return save_process


@step(u'I process "{class_target}" on the "{relative}" side of any "{class_name}" "{value_name}"')
def process_relative_any_object(context, class_target="", relative="", class_name="", value_name=""):
	context.android.process_args['func_name'] = process_relative_any_object
	if class_target and relative and class_name and value_name:
		context.android.process_args["func_args"] = [class_target, relative, class_name, value_name]
	else:
		class_target, relative, class_name, value_name = context.android.process_args["func_args"]
	def save_process():
		ob = context.android.selectAnyObjectBy(value_name, class_name)
		assert ob.exists
		relative_ob = context.android.selectRelativeObjectBy(ob, relative, class_target)
		assert relative_ob.exists	
		return relative_ob
	return save_process


@step(u'I reload process result to temporary value "{key}"')
def reload_process(context, key):
	f = context.android.process_args['func_name'](context)
	ob = f()
	assert ob.exists
	assert context.android.save2InfoTemp(ob, key)


@step(u'I wait object "{key}" exist for "{time_out}"')
def wait_object_exist(context, key, time_out):
	ob = context.android.get2InfoTemp(key)
	assert ob
	assert context.android.waitObjectShow(ob, time_out)


@step(u'I wait object "{key}" gone for "{time_out}"')
def wait_object_gone(context, key, time_out):
	ob = context.android.get2InfoTemp(key)
	assert ob
	assert context.android.waitObjectGone(ob, time_out)
