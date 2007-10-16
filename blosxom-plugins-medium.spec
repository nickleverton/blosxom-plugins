
Name: blosxom-plugins-medium
Summary: Plugins for blosxom, the lightweight blogging application
Version: 2.0.0rc1
Release: 1
Source0: http://downloads.sourceforge.net/blosxom/%{name}-%{version}.tar.gz
License: MIT/GPL/Perl
URL: http://blosxom.sourceforge.net
Group: Applications/Internet
Prefix: /usr/share/blosxom/plugins
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch
Conflicts: blosxom-plugins-small, blosxom-plugins-large
Provides: blosxom-plugins

%description
This package contains a set of plugins for blosxom, the lightweight
blogging application.

%prep
%setup 

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/blosxom/plugins

install -m0644 * %{buildroot}/usr/share/blosxom/plugins

rm -f %{buildroot}/usr/share/blosxom/plugins/*README
rm -f %{buildroot}/usr/share/blosxom/plugins/*LICEN?E
rm -f %{buildroot}/usr/share/blosxom/plugins/*.spec

#install activate_blosxom_ipc %{buildroot}/usr/share/blosxom/plugins

%post
#/usr/share/blosxom/plugins/activate_blosxom_ipc

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/blosxom/plugins/*
%doc README
%doc *.README
%doc *.LICENCE 

%changelog
* Tue Sep 18 2007 Gavin Carr <gavin@openfusion.com.au> 2.0.0-1
- Rename to blosxom-plugins-medium.
- Move content to /usr/share/blosxom/plugins.

* Fri Aug 24 2007 Gavin Carr <gavin@openfusion.com.au> 2.0.0-0
- Initial spec file.

