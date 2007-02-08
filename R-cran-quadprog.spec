%define		fversion	%(echo %{version} |tr r -)
%define		modulename	quadprog
Summary:	Functions to solve Quadratic Programming Problems
Summary:	Funkcje do rozwi±zywania problemów programowania kwadratowego
Name:		R-cran-%{modulename}
Version:	1.4r7
Release:	2
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	d93eb133e72e89de717c9db9d5f28d66
BuildRequires:	R-base >= 2.4.0
BuildRequires:	blas-devel
BuildRequires:	gcc-g77
Requires(post,postun):	R-base >= 2.4.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains routines and documentation for solving quadratic
programming problems.

%description -l pl
Pakiet zawiera biblioteki i dokumentacjê do rozwi±zywania problemów
programowania kwadratowego.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,ChangeLog,README}
%{_libdir}/R/library/%{modulename}
