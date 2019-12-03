#/****************************************************************************
# |
# |     Copyright 2019 Micro Focus. All rights reserved.
# |
# |     This file and all modifications and additions to the pristine
# |     package are under the same license as the package itself.
# |
# +***************************************************************************/

#
# spec file for package supportutils-plugin-mf-smt
#

Name:           supportutils-plugin-mf-smt
Version:        1.0.0
Release:        0
License:        GPL-2.0
Group:          System/Monitoring
Summary:        Supportconfig Plugin for Micro Focus Subscription Management Tool
Url:            http://www.microfocus.com
Source:         mfsmt
#Patch:
#BuildRequires:  supportutils
Requires:  supportutils
ExclusiveArch:  x86_64

%description
Supportconfig plugin for Micro Focus Subscription Management Tool. 

%install
install -d $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -D -m 0544 %{_sourcedir}/mfsmt %{buildroot}/usr/lib/supportconfig/plugins/

%files
%defattr(-,root,root,-)
%dir /usr/lib/supportconfig
%dir /usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/mfsmt

#%clean
#rm -rf $RPM_BUILD_ROOT

#%changelog -n supportutils-plugin-mf-smt
