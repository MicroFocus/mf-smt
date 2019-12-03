#
# spec file for package patterns-smt
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           patterns-mf-smt
BuildRequires:  perl(URI::Escape)
Summary:        Micro Focus Subscription Management Tool
License:        GPL-2.0+
Group:          Metapackages
Version:        12.1
Release:        0
Url:            http://en.opensuse.org/Patterns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  package-translations
Source0:        %name.rpmlintrc


# just for the sources, not in any package (yet)
#Source40:       overview.txt


%{expand:%(perl /usr/share/package-translations/create_macros)}

#BEGIN1

#$%pattern_primaryfunctions
Conflicts:	patterns-smt <= 12
Conflicts:	pattern() = smt
Conflicts:	yast2-smt <= 3.0.0

Provides:       pattern() = mf-smt
#Provides:       pattern-icon() = pattern-generic
Provides:       pattern-icon() = pattern-generic
# TBD
Provides:       pattern-order() = 5060
Provides:       pattern-visible()
#TBD: minimal?
Requires:       pattern() = basesystem
Requires:       pattern() = mf-smt
Requires:	patterns-mf-smt

Requires:	mf-smt
Requires:	supportutils-plugin-mf-smt
Recommends:	yast2-mf-smt
Recommends:	mf-smt-support

#TBD
# Recommends:	sled-smt_en-pdf

%description
This pattern installs the packages for the Micro Focus Subscription Management Tool (SMT).



#END1

%prep
# empty on purpose

%install

#BEGIN2
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-mf-smt
# echo 'This file marks the pattern smt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-smt/smt.txt
echo 'This file marks the pattern mf smt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-mf-smt/mf-smt.txt
#END2

#BEGIN3
%files 
%defattr(-,root,root)
%dir /usr/share/doc/packages
%dir /usr/share/doc/packages/patterns-mf-smt
/usr/share/doc/packages/patterns-mf-smt/mf-smt.txt

#END4

%changelog
