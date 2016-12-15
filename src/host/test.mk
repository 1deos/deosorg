CHECK_FILES:=$(addprefix check.,$(FILES))

deos.check: $(CHECK_FILES)

$(CHECK_FILES):
	@[ -f $(BASEDIR)/$(subst check.,,$@) ]\
		&& echo "\x1b[32;01m$(subst check.,[PASS] CHECK => ,$@)\x1b[0m"\
		|| echo "\x1b[31;01m$(subst check.,[FAIL] CHECK => ,$@)\x1b[0m";
