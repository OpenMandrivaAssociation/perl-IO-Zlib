%define module	IO-Zlib
%define name		perl-%{module}
%define version		1.08
%define release		%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	IO:: style interface to Compress::Zlib
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/IO/%{module}-%{version}.tar.gz
BuildRequires:	perl-Compress-Zlib
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence
to gzip/zlib compressed files. It provides many of the same methods as
the IO::Handle interface.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/IO/*
%{_mandir}/man?/*
