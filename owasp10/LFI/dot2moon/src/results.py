#!/usb/bin/python
#coding: utf-8

from colorama import Fore
from difflib import unified_diff

__AUTHOR__ = "Fnkoc"
__LICENSE__= "MIT"

"""
MIT License

Copyright (c) 2017 Franco Colombino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class show(object):
    def __init__(self, infos, default_size, post):
        self.infos = infos
        self.default_size = default_size
        self.post = post

    #Get the average size of all pages using arithmetical mean
    def AverageSize(self):
        _sizes = []
        
        if self.post != None:
            for s in self.infos:
                _sizes.append(self.infos[s][0])
        else:
            for s in self.infos:
                _sizes.append(self.infos[s][1])
        try:
            avg = round(sum(_sizes)/len(_sizes), 0)
        except TypeError:
            print(" [-] Something went wrong")
            avg = 0

        return(avg)

    #Show details of all pages scanned/found (only code 200)
    def detail(self, average, characters):
        if self.post != None:
            for l in self.infos:
                print("Payload: %s" % l)
                print("Average Size: %s bytes" % average) 
                print("Default Size: %s bytes" % self.default_size)
                print("Size: %s bytes" % self.infos[l][0])
                try:
                    print("HTML:\n%s" % self.infos[l][1][:characters])
                except IndexError:
                    pass
                print(Fore.YELLOW)
                print("-"*80)
                print(Fore.RESET)

        else:
            for l in self.infos:
                print("URL: %s" % l)
                print("HTTP code: %s" % self.infos[l][0])
            
                if l == self.infos[l][2]:
                    pass
                else:
                    print("Redirected to: %s" % self.infos[l][2])

                print("Average Size: %s bytes" % average) 
                print("Default Size: %s bytes" % self.default_size)
                print("Size: %s bytes" % self.infos[l][1])
                try:
                    print("HTML:\n%s" % self.infos[l][5][:characters])
                except IndexError:
                    pass
                print(Fore.YELLOW)
                print("-"*80)
                print(Fore.RESET)

    #Funtion that will only show the potential results
    def potential(self, average, characters, default_html):
        default_html = default_html.splitlines()

        print(Fore.GREEN)
        print("-"*80)
        print("----POTENTIAL-RESULTS" + ("-" * 59))
        print("-"*80)
        print(Fore.RESET)
        if self.post != None:
            for l in self.infos:
                print("Payload: %s" % l)
                print("Average Size: %s bytes" % average) 
                print("Default Size: %s bytes" % self.default_size)
                print("Size: %s bytes" % self.infos[l][0])
                try:
                    print(Fore.CYAN)
                    target_html = self.infos[l][1].splitlines()
                    diff = unified_diff(
                            default_html, target_html, lineterm="\n")

                    for content in diff:
                        if content[0] == "+":
                            print(content[1:])

                    print(Fore.RESET)
                except IndexError:
                    pass
        else:
            for l in self.infos:
                if len(self.infos[l]) == 5:
                    print("URL: %s" % l)
                    print("HTTP code: %s" % self.infos[l][0])
            
                    if l == self.infos[l][2]:
                        pass
                    else:
                        print("Redirected to: %s" % self.infos[l][2])

                    print("Average Size: %s bytes" % average) 
                    print("Default Size: %s bytes" % self.default_size)
                    print("Size: %s bytes" % self.infos[l][1])
                    try:
                        print(Fore.CYAN)
                        target_html = self.infos[l][4].splitlines()
                        diff = unified_diff(
                                default_html, target_html, lineterm="\n")

                        for content in diff:
                            if content[0] == "+":
                                print(content[1:])

                        print(Fore.RESET)
                    except IndexError:
                        pass
                    print(Fore.YELLOW)
                    print("-"*80)
                    print(Fore.RESET)

    def output(self, file_name, average):
        with open(file_name, "w") as f:
            for l in self.infos:
                f.write("URL: %s\n" % l)
                f.write("HTTP code: %s\n" % self.infos[l][0])
            
                if l == self.infos[l][2]:
                    pass
                else:
                    f.write("Redirected to: %s\n" % self.infos[l][2])

                f.write("Average Size: %s bytes\n" % average) 
                f.write("Default Size: %s bytes\n" % self.default_size)
                f.write("Size: %s bytes\n" % self.infos[l][1])
                try:
                    f.write("HTML:\n%s\n" % self.infos[l][4])
                except IndexError:
                    pass
                f.write("-"*80)
                f.write("\n")

            f.write("\n")
            f.write("-" * 80)
            f.write("\n----POTENTIAL-RESULTS" + ("-" * 59))
            f.write("-" * 80)
            f.write("\n")

            for l in self.infos:
                if len(self.infos[l]) == 5:
                    f.write("URL: %s\n" % l)
                    f.write("HTTP code: %s\n" % self.infos[l][0])
            
                    if l == self.infos[l][2]:
                        pass
                    else:
                        f.write("Redirected to: %s\n" % self.infos[l][2])

                    f.write("Average Size: %s bytes\n" % average) 
                    f.write("Default Size: %s bytes\n" % self.default_size)
                    f.write("Size: %s bytes\n" % self.infos[l][1])
                    try:
                        f.write("HTML:\n%s\n" % self.infos[l][4])
                    except IndexError:
                        pass
                    f.write("-"*80)
                    f.write("\n")
