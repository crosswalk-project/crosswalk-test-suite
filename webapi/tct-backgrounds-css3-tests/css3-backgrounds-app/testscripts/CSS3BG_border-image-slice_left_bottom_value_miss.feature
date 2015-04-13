Feature: css3-backgrounds
 Scenario: CSS3BG border image slice left bottom value miss
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/CSS3BG_border-image-slice_left_bottom_value_miss-manual.html"
     And I save the page to "CSS3BG_border-image-slice_left_bottom_value_miss"
     And I save the screenshot md5 as "CSS3BG_border-image-slice_left_bottom_value_miss"
    Then file "CSS3BG_border-image-slice_left_bottom_value_miss" of baseline and result should be the same
