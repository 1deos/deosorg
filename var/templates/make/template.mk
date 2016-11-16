# <T> Makefile

<T>: <T>.build <T>.run.pre <T>.run <T>.run.post
	@

<T>.build: <T>.clean
	@

<T>.run.new:
	@
	@$(PRINT) red <T> start

<T>.run.pre: <T>.run.new
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(PRINT) blue <T>.run start

<T>.run:
	@

<T>.run.post:
	@$(PRINT) blue <T>.run stop
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(MAKE) <T>.run.free

<T>.run.free:
	@echo
	@$(PRINT) red <T> stop

<T>.clean:
	@clear
