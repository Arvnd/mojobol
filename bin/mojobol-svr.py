#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/opt/mojobol/libs")
from mojobol import *
from datetime import *
from mojoasteriskplayer import *
if __name__=="__main__":
	env=read_agi_environment()
	ms=MojoBolResponder("/opt/voh/voh.conf")
	call=MojoBolCall(ms,env)
	p=call.responder.parse_workflow(call)
	call.endcall()
	call.compresscallfile()
