Δ with (data=None)

export MAKEFLAGS=Δ(data['makeflags'])

.DEFAULT_GOAL:=Δ(data['default_goal'])

.PHONY:Δ(data['phony'])

.SUBLIME_TARGETS:Δ(data['sublime_targets'])

include Δ(data['config_file'])

all: #init build
	Δ(data['all']['hook']['pre'])
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	Δ(data['all']['if:host;is:mac'])
else
	Δ(data['all']['else'])
endif
	Δ(data['all']['hook']['post'])
