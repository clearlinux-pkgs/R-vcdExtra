#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-vcdExtra
Version  : 0.8.5
Release  : 53
URL      : https://cran.r-project.org/src/contrib/vcdExtra_0.8-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vcdExtra_0.8-5.tar.gz
Summary  : 'vcd' Extensions and Additions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ca
Requires: R-dplyr
Requires: R-glue
Requires: R-gnm
Requires: R-here
Requires: R-purrr
Requires: R-readxl
Requires: R-stringr
Requires: R-tidyr
Requires: R-vcd
BuildRequires : R-ca
BuildRequires : R-dplyr
BuildRequires : R-glue
BuildRequires : R-gnm
BuildRequires : R-here
BuildRequires : R-purrr
BuildRequires : R-readxl
BuildRequires : R-stringr
BuildRequires : R-tidyr
BuildRequires : R-vcd
BuildRequires : buildreq-R

%description
and the 'gnm' package for Generalized Nonlinear Models.
	In particular, 'vcdExtra' extends mosaic, assoc and sieve plots from 'vcd' to handle 'glm()' and 'gnm()' models and
	adds a 3D version in 'mosaic3d'.  Additionally, methods are provided for comparing and visualizing lists of
	'glm' and 'loglm' objects. This package is now a support package for the book, "Discrete Data Analysis with R" by
  Michael Friendly and David Meyer.

%prep
%setup -q -n vcdExtra
pushd ..
cp -a vcdExtra buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692718883

%install
export SOURCE_DATE_EPOCH=1692718883
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vcdExtra/DESCRIPTION
/usr/lib64/R/library/vcdExtra/INDEX
/usr/lib64/R/library/vcdExtra/Meta/Rd.rds
/usr/lib64/R/library/vcdExtra/Meta/data.rds
/usr/lib64/R/library/vcdExtra/Meta/demo.rds
/usr/lib64/R/library/vcdExtra/Meta/features.rds
/usr/lib64/R/library/vcdExtra/Meta/hsearch.rds
/usr/lib64/R/library/vcdExtra/Meta/links.rds
/usr/lib64/R/library/vcdExtra/Meta/nsInfo.rds
/usr/lib64/R/library/vcdExtra/Meta/package.rds
/usr/lib64/R/library/vcdExtra/Meta/vignette.rds
/usr/lib64/R/library/vcdExtra/NAMESPACE
/usr/lib64/R/library/vcdExtra/NEWS.md
/usr/lib64/R/library/vcdExtra/R/vcdExtra
/usr/lib64/R/library/vcdExtra/R/vcdExtra.rdb
/usr/lib64/R/library/vcdExtra/R/vcdExtra.rdx
/usr/lib64/R/library/vcdExtra/WORDLIST
/usr/lib64/R/library/vcdExtra/data/Rdata.rdb
/usr/lib64/R/library/vcdExtra/data/Rdata.rds
/usr/lib64/R/library/vcdExtra/data/Rdata.rdx
/usr/lib64/R/library/vcdExtra/demo/Wong2-3.R
/usr/lib64/R/library/vcdExtra/demo/Wong3-1.R
/usr/lib64/R/library/vcdExtra/demo/housing.R
/usr/lib64/R/library/vcdExtra/demo/mental-glm.R
/usr/lib64/R/library/vcdExtra/demo/mosaic3d-demo.R
/usr/lib64/R/library/vcdExtra/demo/mosaic3d-hec.R
/usr/lib64/R/library/vcdExtra/demo/occStatus.R
/usr/lib64/R/library/vcdExtra/demo/ucb-glm.R
/usr/lib64/R/library/vcdExtra/demo/vision-quasi.R
/usr/lib64/R/library/vcdExtra/demo/yaish-unidiff.R
/usr/lib64/R/library/vcdExtra/demo/yamaguchi-xie.R
/usr/lib64/R/library/vcdExtra/doc/continuous.R
/usr/lib64/R/library/vcdExtra/doc/continuous.Rmd
/usr/lib64/R/library/vcdExtra/doc/continuous.html
/usr/lib64/R/library/vcdExtra/doc/creating.R
/usr/lib64/R/library/vcdExtra/doc/creating.Rmd
/usr/lib64/R/library/vcdExtra/doc/creating.html
/usr/lib64/R/library/vcdExtra/doc/datasets.R
/usr/lib64/R/library/vcdExtra/doc/datasets.Rmd
/usr/lib64/R/library/vcdExtra/doc/datasets.html
/usr/lib64/R/library/vcdExtra/doc/demo-housing.R
/usr/lib64/R/library/vcdExtra/doc/demo-housing.Rmd
/usr/lib64/R/library/vcdExtra/doc/demo-housing.html
/usr/lib64/R/library/vcdExtra/doc/index.html
/usr/lib64/R/library/vcdExtra/doc/loglinear.R
/usr/lib64/R/library/vcdExtra/doc/loglinear.Rmd
/usr/lib64/R/library/vcdExtra/doc/loglinear.html
/usr/lib64/R/library/vcdExtra/doc/mobility.R
/usr/lib64/R/library/vcdExtra/doc/mobility.Rmd
/usr/lib64/R/library/vcdExtra/doc/mobility.html
/usr/lib64/R/library/vcdExtra/doc/mosaics.R
/usr/lib64/R/library/vcdExtra/doc/mosaics.Rmd
/usr/lib64/R/library/vcdExtra/doc/mosaics.html
/usr/lib64/R/library/vcdExtra/doc/tests.R
/usr/lib64/R/library/vcdExtra/doc/tests.Rmd
/usr/lib64/R/library/vcdExtra/doc/tests.html
/usr/lib64/R/library/vcdExtra/extdata/tv.dat
/usr/lib64/R/library/vcdExtra/extdata/vcdExtra-datasets.xlsx
/usr/lib64/R/library/vcdExtra/help/AnIndex
/usr/lib64/R/library/vcdExtra/help/aliases.rds
/usr/lib64/R/library/vcdExtra/help/figures/logo.png
/usr/lib64/R/library/vcdExtra/help/paths.rds
/usr/lib64/R/library/vcdExtra/help/vcdExtra.rdb
/usr/lib64/R/library/vcdExtra/help/vcdExtra.rdx
/usr/lib64/R/library/vcdExtra/html/00Index.html
/usr/lib64/R/library/vcdExtra/html/R.css
