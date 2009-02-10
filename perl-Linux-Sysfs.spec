%define module Linux-Sysfs
%define name perl-%{module}

Summary:	Perl interface to libsysfs
Name:		%{name}
Version:	0.03
Release:	%mkrel 1
License:	LGPLv2+
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Linux/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	libsysfs-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This module implements an interface to the kernel's sysfs
filesystem.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/systool.pl
%{perl_vendorarch}/Linux
%{perl_vendorarch}/auto/Linux
%{_mandir}/man3/*
