#!/usr/bin/env python

from atip.common.steps import *
from atip.web.steps import *
import time
import datetime
import md5
import Image

#get md5 of a input string  
def get_string_md5(str):  
    m = md5.new()  
    m.update(str)  
    return m.hexdigest()  

#standardize the image 
def make_regalur_image(img, size = (256, 256)):
    return img.resize(size).convert('RGB')

def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

#Images similarity calculation
def cal_images_similar(img1,img2):
   #open two images
   fimg1=Image.open(img1)
   fimg2=Image.open(img2)
   #img2=Image.open("./pic.png") 

   #regular the image
   reg_img1 = make_regalur_image(fimg1)
   reg_img2 = make_regalur_image(fimg2)

   #calculate the similar 
   ret=hist_similar(reg_img1.histogram(), reg_img2.histogram())
   return ret*100  

@step(u'I press "{key_prefix}" for {n:d} times cyclically')
def i_press_cycle(context, key_prefix, n):
    for i in range(1,n+1):
      for j in range(i,n+1):
        key1 = key_prefix + str(i)
	#print "key:" + key1
	assert context.app.press_element_by_key(key1)
        time.sleep(1)
        key2 = key_prefix + str(j)
	assert context.app.press_element_by_key(key2)
        time.sleep(0.1)

@step(u'I verify "{text}" with link "{link}"')
def check_link_by_text(context, link, text):
   element = context.app.driver.find_element_by_link_text(text)
   #print "hyperlink:" , element.get_attribute('href')
   #print "link:", link
   hyperlink = element.get_attribute('href')
   #assert element.get_attribute('href') == link
   if hyperlink == link:
      assert True
   else:
      assert False


@step(u'I click button with class "{classname}" and text "{text}"')
def click_button_by_class_and_text(context, classname, text):
   elements = context.app.driver.find_elements_by_class_name(classname)
   length = len(elements) 
   for i in range(0,length):
     #print "loop i:", i
     if elements[i].text == "START":
	#print "clicki:", i
	#print "text:", elements[i].text
	elements[i].click()
	assert True

@step(u'I wait {n:d} seconds')
def wait_senconds(context,n):
   time.sleep(n) 

@step(u'I check screenshot should be "{exp_md5}"')
def i_check_screenshot_base64_md5(context, exp_md5):
   pic_base64 = context.app.driver.get_screenshot_as_base64()
   #context.app.driver.get_screenshot_as_file("/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/pic.png")
   pic_md5 = get_string_md5(pic_base64)
   print "pic_md5", pic_md5
   print "exp_md5", exp_md5
   if pic_md5 == exp_md5:
      assert True
   else:
      assert False

@step(u'I check screenshot "{img}" should have {percent:d} similarity with "{baseline_img}"')
def i_check_screenshot(context, img, baseline_img, percent ):
   context.app.driver.get_screenshot_as_file(img)
   #print "screenshot:", img
   #print "baseline img:", baseline_img
   similarity = cal_images_similar(img,baseline_img)
   print "similarity:", similarity
   if similarity > percent:
      print "similarity:", similarity
      assert True
   else:   
      assert False

def compare_values(value1, value2, num):
   times = value2/value1;
   if times >= num:
      assert True
   else:
      assert False

@step(u'I check "{eid}" is {num:f} times after click "{eid2}" for {nsec:d} seconds')
def I_compare_values(context, eid, num, eid2, nsec):
   element = context.app.driver.find_element_by_id(eid)
   text = element.text; 
   value_start = float(text);
   element = context.app.driver.find_element_by_id(eid2)
   #print "element2:", element.text
   element.click()
   time.sleep(nsec)
   element = context.app.driver.find_element_by_id(eid)     
   text = element.text;
   value_end = float(text);    
   compare_values(value_start, value_end, num)


