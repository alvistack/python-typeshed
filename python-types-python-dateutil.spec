# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-types-python-dateutil
Epoch: 100
Version: 2.8.19.14
Release: 1%{?dist}
BuildArch: noarch
Summary: Typing stubs for python-dateutil
License: Apache-2.0
URL: https://pypi.org/project/types-python-dateutil/#history
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This is a PEP 561 type stub package for the python-dateutil package. It
can be used by type-checking tools like mypy, pyright, pytype, PyCharm,
etc. to check code that uses python-dateutil.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-types-python-dateutil
Summary: Typing stubs for python-dateutil
Requires: python3
Provides: python3-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python3dist(types-python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(types-python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(types-python-dateutil) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-types-python-dateutil
This is a PEP 561 type stub package for the python-dateutil package. It
can be used by type-checking tools like mypy, pyright, pytype, PyCharm,
etc. to check code that uses python-dateutil.

%files -n python%{python3_version_nodots}-types-python-dateutil
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-types-python-dateutil
Summary: Typing stubs for python-dateutil
Requires: python3
Provides: python3-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python3dist(types-python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(types-python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(types-python-dateutil) = %{epoch}:%{version}-%{release}

%description -n python3-types-python-dateutil
This is a PEP 561 type stub package for the python-dateutil package. It
can be used by type-checking tools like mypy, pyright, pytype, PyCharm,
etc. to check code that uses python-dateutil.

%files -n python3-types-python-dateutil
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-types-python-dateutil
Summary: Typing stubs for python-dateutil
Requires: python3
Provides: python3-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python3dist(types-python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(types-python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-types-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(types-python-dateutil) = %{epoch}:%{version}-%{release}

%description -n python3-types-python-dateutil
This is a PEP 561 type stub package for the python-dateutil package. It
can be used by type-checking tools like mypy, pyright, pytype, PyCharm,
etc. to check code that uses python-dateutil.

%files -n python3-types-python-dateutil
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
