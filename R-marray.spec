%global packname  marray
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.32.0
Release:          1
Summary:          Exploratory analysis for two-color spotted microarray data
Group:            Sciences/Mathematics
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/marray.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/marray_1.32.0.tar.gz
Requires:         R-limma R-methods 
Requires:         R-tkWidgets 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-limma R-methods
BuildRequires:    R-tkWidgets 

%description
Class definitions for two-color spotted microarray data. Fuctions for data
input, diagnostic plots, normalization and quality checking.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/swirldata
