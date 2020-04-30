################################################################################
#
# detect-overwrite
#
################################################################################

define DETECT_OVERWRITE_INSTALL_TARGET_CMDS
	grep -q "^foo" $(TARGET_DIR)/etc/passwd || \
		echo "foo" >> $(TARGET_DIR)/etc/passwd
endef

HOST_DETECT_OVERWRITE_DEPENDENCIES = host-pkgconf

define HOST_DETECT_OVERWRITE_INSTALL_CMDS
	$(SED) 's/manipulating/tweaking/' $(HOST_DIR)/lib/pkgconfig/libpkgconf.pc
endef

$(eval $(generic-package))
$(eval $(host-generic-package))
