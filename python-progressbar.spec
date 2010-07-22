%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define realname progressbar

Name:           python-%{realname}
Version:        2.2
Release:        8%{?dist}
Summary:        Text progressbar library for python

Group:          Development/Libraries
License:        LGPLv2+ 
URL:            http://pypi.python.org/pypi/%{realname}/
Source0:        http://pypi.python.org/packages/source/p/%{realname}/%{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildArch:      noarch

%description

This library provides a text mode progress bar. This is typically used to 
display the progress of a long running operation, providing a visual clue that 
processing is under way.

The progressbar module is very easy to use, yet very powerful. And 
automatically supports features like auto-resizing when available.

%prep
%setup -q -n %{realname}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
chmod 0755 $RPM_BUILD_ROOT/%{python_sitelib}/progressbar.py
 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE
%doc README
%{python_sitelib}/*

%changelog
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
