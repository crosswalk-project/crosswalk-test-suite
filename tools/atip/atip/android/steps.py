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


@step(u'I launch "{app_name}" with "{apk_pkg_name}" and "{apk_activity_name}" on android')
def launch_app_by_names(context, app_name, apk_pkg_name, apk_activity_name):
    android.launch_app_by_name(
        context,
        app_name,
        apk_pkg_name,
        apk_activity_name)


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


@step(u'I should see view "{params_kw}"')
def select_view_by(context, params_kw):
    ob = context.android.selectObjectBy(params_kw)
    assert ob.exists


@step(u'I should see relative view "{params_kw1}" on the "{position}" side of view "{params_kw2}"')
def select_relative_object(context, params_kw1, position, params_kw2):
    ob = context.android.selectObjectBy(params_kw2)
    assert ob.exists
    assert context.android.selectRelativeObjectBy(ob, position, params_kw1).exists


@step(u'I should not see view "{params_kw}"')
def select_noneview_by(context, params_kw):
    ob = context.android.selectObjectBy(params_kw)
    assert not ob.exists


@step(u'I should not see relative view "{params_kw1}" on the "{position}" side of view "{params_kw2}"')
def select_relative_noneobject(context, params_kw1, position, params_kw2):
    ob = context.android.selectObjectBy(params_kw2)
    assert not ob.exists
    assert not context.android.selectRelativeObjectBy(ob, position, params_kw1).exists


@step(u'I click view "{params_kw}"')
def click_view(context, params_kw):
    ob = context.android.selectObjectBy(params_kw)
    assert ob.exists
    assert context.android.clickObject(ob)


@step(u'I click saved object "{key}"')
def click_object(context, key):
    ob = context.android.get2InfoTemp(key)
    assert ob.exists
    assert context.android.clickObject(ob)


@step(u'I edit view "{params_kw}" to input "{text}"')
def set_edittext_object(context, params_kw, text):
    ob = context.android.selectObjectBy(params_kw)
    assert ob.exists
    assert context.android.setEditText(ob, text)


@step(u'I edit index {n:d} EditText to input "{text}"')
def set_index_edittext_object(context, n, text):
    ob = context.android.selectObjectBy("className=android.widget.EditText")[n]
    assert ob.exists
    assert context.android.setEditText(ob, text)


@step(u'I save view "{params_kw}" to object "{key}"')
def save_view_to_object(context, params_kw, key):
    ob = context.android.selectObjectBy(params_kw)
    assert ob.exists
    assert context.android.save2InfoTemp(ob, key)


@step(u'I save relative view "{params_kw1}" on the "{position}" side of view "{params_kw2}" to object "{key}"')
def save_relativeview_to_object(context, params_kw1, position, params_kw2, key):
    ob = context.android.selectObjectBy(params_kw2)
    assert ob.exists
    relative_ob = context.android.selectRelativeObjectBy(ob, position, params_kw1)
    assert relative_ob.exists
    assert context.android.save2InfoTemp(relative_ob, key)


@step(u'I save object "{key}" info "{info_name}" to temp "{info_key}"')
def save_info_temp(context, key, info_name, info_key):
    ob = context.android.get2InfoTemp(key)
    info = context.android.getObjectInfo(ob, info_name)
    assert context.android.save2InfoTemp(info, info_key)


@step(u'The view "{params_kw}" info "{info_name}" should be "{except_result}"')
def compare_views(context, params_kw, info_name, except_result):
    ob = context.android.selectObjectBy(params_kw)
    assert ob.exists
    if context.android.getObjectInfo(ob, info_name) == except_result:
        assert True
    else:
        assert False


@step(u'The saved info "{key1}" is equal to "{key2}"')
def equal_with_keys(context, key1, key2):
    info1 = context.android.get2InfoTemp(key1)
    info2 = context.android.get2InfoTemp(key2)
    if info1 == info2:
        assert True
    else:
        assert False


@step(u'The saved info "{key1}" is unequal to "{key2}"')
def unequal_with_keys(context, key1, key2):
    info1 = context.android.get2InfoTemp(key1)
    info2 = context.android.get2InfoTemp(key2)
    if info1 != info2:
        assert True
    else:
        assert False


@step(u'I scroll to end')
def scroll_to_end(context):
    assert context.android.scrollToEnd()


@step(u'I fling "{orientation}" goto "{direction}"')
def fling_by(context, orientation, direction):
    assert context.android.flingBy(orientation, direction)


@step(u'I swipe view "{params_kw}" to "{orientation}"')
def swipe_to(context, key, orientation):
    ob = context.android.selectObjectBy(params_kw)
    assert ob.exists
    assert context.android.swipeTo(ob, orientation)


@step(u'I swipe saved object "{key}" to "{orientation}"')
def swipe_to(context, key, orientation):
    ob = context.android.get2InfoTemp(key)
    assert ob.exists
    assert context.android.swipeTo(ob, orientation)


@step(u'I save process of finding view "{params_kw1}" on the "{position}" side of view "{params_kw2}"')
def process_finding_relative_view(context, params_kw1="", position="", params_kw2=""):
    context.android.process_args['func_name'] = process_finding_relative_view
    if params_kw1 and position and params_kw2:
        context.android.process_args["func_args"] = [params_kw1, position, params_kw2]
    else:
        params_kw1, position, params_kw2 = context.android.process_args["func_args"]
    def save_process():
        ob = context.android.selectObjectBy(params_kw2)
        assert ob.exists
        relative_ob = context.android.selectRelativeObjectBy(ob, position, params_kw1)
        assert relative_ob.exists
        return relative_ob
    return save_process


@step(u'I reload above process and save result to object "{key}"')
def reload_process(context, key):
    f = context.android.process_args['func_name'](context)
    ob = f()
    assert ob.exists
    assert context.android.save2InfoTemp(ob, key)


@step(u'I wait saved object "{key}" exist in "{time_out}" seconds')
def wait_object_exist(context, key, time_out):
    ob = context.android.get2InfoTemp(key)
    assert ob
    assert context.android.waitObjectShow(ob, time_out)


@step(u'I wait saved object "{key}" gone in "{time_out}" seconds')
def wait_object_gone(context, key, time_out):
    ob = context.android.get2InfoTemp(key)
    assert ob
    assert context.android.waitObjectGone(ob, time_out)