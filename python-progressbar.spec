%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global realname progressbar
%global with_python3 1

Name:           python-%{realname}
Version:        2.3
Release:        6%{?dist}
Summary:        Text progressbar library for python

Group:          Development/Libraries
License:        LGPLv2+ 
URL:            http://code.google.com/p/%{name}/
Source0:        https://%{name}.googlecode.com/files/%{realname}-%{version}.tar.gz
Patch0:         progressbar-interrupt.patch
Patch1:         10_python3.3_compat.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # if with_python3
BuildArch:      noarch

%description

This library provides a text mode progress bar. This is typically used to 
display the progress of a long running operation, providing a visual clue that 
processing is under way.

The progressbar module is very easy to use, yet very powerful. And 
automatically supports features like auto-re-sizing when available.

%if 0%{?with_python3}
%package -n python3-%{realname}
Summary:        Text progressbar library for python

%description -n python3-%{realname}
An python module which provides a convenient example.
%endif # with_python3

%prep
%setup -qc
mv %{realname}-%{version} python2
pushd python2
cp -pr LICENSE.txt README.txt ../
%patch0 -p1 -b .interrupt
%patch1 -p1
popd

%if 0%{?with_python3}
cp -a python2 python3
%endif # with_python3


%build
pushd python2
%{__python} setup.py build
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py build
popd
%endif # with_python3


%install
rm -rf $RPM_BUILD_ROOT
pushd python2
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%doc README.txt
%{python_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{realname}
%defattr(-,root,root,-)
%doc LICENSE.txt
%doc README.txt
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Wed Jul 29 2015 Michael Jeanson <mjeanson@gmail.com> - 2.3-6
- Added python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

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
