#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    fortunes = [
        "Always take the path less traveled; there's less traffic.",
        "Early to bed, early to rise, makes a man an anomaly these days.",
        "Two wrongs don't make a right, but two Wrights make a plane.",
        "Fortunes are earned, not given; however, they can be taken."
    ]

    return random.choice(fortunes)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = 'Your fortune: ' + fortune
        fortune_paragraph = '<p>' + fortune_sentence + '</p>'

        lucky_number = "<strong>" + str(random.randint(1,100)) + "</strong>"
        number_sentence = 'Your lucky number: ' + lucky_number
        number_paragraph = '<p>' + number_sentence + '</p>'

        new_cookie_button = '<a href="."><button>Another cookie, please!</button></a>'

        content = header + fortune_paragraph + number_paragraph + new_cookie_button

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
