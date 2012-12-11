%define upstream_name Linux-Sysfs
%define upstream_version 0.03

Summary:	Perl interface to libsysfs
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	LGPLv2+
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	sysfsutils-devel

%description
This module implements an interface to the kernel's sysfs
filesystem.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/systool.pl
%{perl_vendorarch}/Linux
%{perl_vendorarch}/auto/Linux
%{_mandir}/man3/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.30.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 555999
- rebuild for perl 5.12

* Wed Jul 29 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404046
- rebuild using %%perl_convert_version

* Tue Feb 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.03-1mdv2009.1
+ Revision: 339253
- add source and spec files
- create perl-Linux-Sysfs

