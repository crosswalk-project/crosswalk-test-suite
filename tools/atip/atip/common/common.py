# Copyright (c) 2014 Intel Corporation.
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
#         Fan, Yugang <yugang.fan@intel.com>

APP_TYPE_WEB = "WEB"
APP_TYPE_WGT = "WGT"

import Image
import string
import os
import md5

class APP():

    def __init__(self, app_config=None, app_name=None, timeout=2):
        pass

    def quit(self):
        pass

    #standardize the image
    def make_regalur_image(self, img, size = (256, 256)):
        return img.resize(size).convert('RGB')

    def hist_similar(self, lh, rh):
        assert len(lh) == len(rh)
        return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

    #Images similarity calculation
    def cal_images_similar(self, img1, img2):
        fimg1=Image.open(img1)
        fimg2=Image.open(img2)
        reg_img1 = self.make_regalur_image(fimg1)
        reg_img2 = self.make_regalur_image(fimg2)

        #calculate the similar
        ret= self.hist_similar(reg_img1.histogram(), reg_img2.histogram())
        return ret*100

    def convert_pic(self, pic_name, ratio):
        im = Image.open(pic_name)
        smalling = im.resize(ratio, Image.ANTIALIAS)
        smalling.save(pic_name, "png")
        
    def crop_pic(self, page_pic, element_pic, box):
        im = Image.open(page_pic)
        regin = im.crop(box)
        regin.save(element_pic, "png")

    def check_pic_same(self, pic1, pic2, similarity):
        try:
           pic_similarity = self.cal_images_similar(pic1, pic2)
           if pic_similarity >= string.atoi(similarity):
              return True
           else:
              print "The similarity is: %s" % pic_similarity
              return False
        except Exception as e:
           print "Check similarity failed: %s" % e
           return False

    def check_pic_different(self, pic1, pic2, similarity):
        pic_similarity = self.cal_images_similar(pic1, pic2)
        if pic_similarity >= string.atoi(similarity):
           print "The similarity is: %s" % pic_similarity
           return False
        else:
           return True

    def get_string_md5(self,data_str):
        m = md5.new()
        m.update(data_str)
        return m.hexdigest()
  
