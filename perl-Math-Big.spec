#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Big
Summary:	Math::Big - useful routines and packages with Math::BigInt/BigFloat
Summary(pl.UTF-8):	Math::Big - przydatne funkcje i pakiety oparte o Math::BigInt/BigFloat
Name:		perl-Math-Big
Version:	1.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5782c961f405e04c2bf1bcde309c24d2
URL:		http://search.cpan.org/dist/Math-Big/
BuildRequires:	perl-Math-BigInt >= 1.74
BuildRequires:	perl(Math::BigFloat) >= 1.48
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.74
Requires:	perl(Math::BigFloat) >= 1.48
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Big module contains some routines that may come in handy when
you want to do some math with really, really big (or small) numbers.

%description -l pl.UTF-8
Moduł Math::Big zawiera trochę procedur, które mogą okazać się pomocne
przy obróbce bardzo, bardzo dużych (lub małych) liczb.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BENCHMARK BUGS CHANGES CREDITS LICENSE NEW README TODO
%{perl_vendorlib}/Math/Big.pm
%{perl_vendorlib}/Math/Big
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.txt
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
