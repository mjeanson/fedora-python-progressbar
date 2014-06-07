%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define realname progressbar

Name:           python-%{realname}
Version:        2.3
Release:        4%{?dist}
Summary:        Text progressbar library for python

Group:          Development/Libraries
License:        LGPLv2+ 
URL:            http://code.google.com/p/%{name}/
Source0:        https://%{name}.googlecode.com/files/%{realname}-%{version}.tar.gz
Patch0:         progressbar-interrupt.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch:      noarch

%description

This library provides a text mode progress bar. This is typically used to 
display the progress of a long running operation, providing a visual clue that 
processing is under way.

The progressbar module is very easy to use, yet very powerful. And 
automatically supports features like auto-re-sizing when available.

%prep
%setup -q -n %{realname}-%{version}

%patch0 -p1 -b .interrupt

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%doc README.txt
%{python_sitelib}/*

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 25 2013 Christof Damian <christof@damian.net> - 2.3-2
- added interrupt patch bug #965919

* Sat Apr 27 2013 Christof Damian <christof@damian.net> - 2.3-1
- upstream 2.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 8 2009 Christof Damian <christof@damian.net> 2.2-5
- don't include sitelib in files 

* Thu Jan 8 2009 Christof Damian <christof@damian.net> 2.2-4
- change the attributes of progressbar.py in install

* Thu Jan 8 2009 Christof Damian <christof@damian.net> 2.2-3
- changed attributes for progressbar.py, it contains excuteable examples

* Tue Jan 6 2009 Christof Damian <christof@damian.net> 2.2-2
- remove version from upstream url

* Sat Jan 3 2009 Christof Damian <christof@damian.net> 2.2-1
- initial spec file
