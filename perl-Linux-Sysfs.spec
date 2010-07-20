%define upstream_name Linux-Sysfs
%define upstream_version 0.03

Summary:	Perl interface to libsysfs
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2
License:	LGPLv2+
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	libsysfs-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This module implements an interface to the kernel's sysfs
filesystem.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
