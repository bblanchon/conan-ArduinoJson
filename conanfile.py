#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ArduinoJsonConan(ConanFile):
    name = "ArduinoJson"
    version = "5.12.0"
    url = "https://github.com/bincrafters/conan-ArduinoJson"
    description = "An efficient and elegant JSON library for Arduino. ArduinoJson supports ✔ serialization, ✔ deserialization, ✔ fixed allocation, ✔ zero-copy, ✔ streams, and more. It is the most popular Arduino library on GitHub ❤. Check out arduinojson.org for a comprehensive documentation."
    license = "https://github.com/someauthor/ArduinoJson/blob/master/LICENSE"
    exports_sources = ["LICENSE"]

    def source(self):
        source_url = "https://github.com/bblanchon/ArduinoJson"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")
        #Rename to "sources" is a convention to simplify later steps

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="sources")
        self.copy(pattern="*", dst="include", src=os.path.join("sources", "src"))

    def package_id(self):
        self.info.header_only()
