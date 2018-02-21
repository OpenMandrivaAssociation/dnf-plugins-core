%{?!dnf_lowest_compatible: %global dnf_lowest_compatible 2.7.0}
%{?!dnf_not_compatible: %global dnf_not_compatible 3.0}
%global dnf_plugins_extra 2.0.0
%global hawkey_version 0.8.0

# Copr targets are not available for OpenMandriva
%bcond_with copr_plugin

# Enable Python 3 by default
%bcond_without python3

# OpenMandriva has never used Yum, so we don't need the yum migrator plugin
%bcond_with yum_migrate

Name:       dnf-plugins-core
Version:    2.1.5
Release:    1
Summary:    Core Plugins for DNF
Group:      System/Configuration/Packaging
License:    GPLv2+
URL:        https://github.com/rpm-software-management/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz


# OpenMandriva specific patches
Patch1001:  dnf-plugins-core-2.1.5-Fix-detection-of-Python-2.patch

BuildArch:  noarch

BuildRequires:  cmake
BuildRequires:  gettext
%if %{with python3}
Requires:   python-dnf-plugins-core = %{version}-%{release}
%else
Requires:   python2-dnf-plugins-core = %{version}-%{release}
%endif
Provides:   dnf-command(builddep)
Provides:   dnf-command(config-manager)
%if %{with copr_plugin}
Provides:   dnf-command(copr)
%endif
Provides:   dnf-command(debug-dump)
Provides:   dnf-command(debug-restore)
Provides:   dnf-command(debuginfo-install)
Provides:   dnf-command(download)
Provides:   dnf-command(repoclosure)
Provides:   dnf-command(repograph)
Provides:   dnf-command(repomanage)
Provides:   dnf-command(reposync)

# Plugins shift from extras to core
Provides:   dnf-plugins-extras-debug = %{version}-%{release}
Provides:   dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:   dnf-plugins-extras-repograph = %{version}-%{release}
Provides:   dnf-plugins-extras-repomanage = %{version}-%{release}
# Generic package name Provides
Provides:   dnf-plugin-builddep = %{version}-%{release}
Provides:   dnf-plugin-config-manager = %{version}-%{release}
Provides:   dnf-plugin-debuginfo-install = %{version}-%{release}
Provides:   dnf-plugin-download = %{version}-%{release}
Provides:   dnf-plugin-generate_completion_cache = %{version}-%{release}
Provides:   dnf-plugin-needs_restarting = %{version}-%{release}
Provides:   dnf-plugin-repoclosure = %{version}-%{release}
Provides:   dnf-plugin-repograph = %{version}-%{release}
Provides:   dnf-plugin-repomanage = %{version}-%{release}
Provides:   dnf-plugin-reposync = %{version}-%{release}

Conflicts:  dnf-plugins-extras-common-data < %{dnf_plugins_extra}


%description
Core Plugins for DNF. This package enhances DNF with the builddep, config-manager,
%{?_with_copr_plugin:copr, }debug, debuginfo-install, download, needs-restarting,
repoclosure, repograph, repomanage, and reposync commands. Additionally, it provides
the generate_completion_cache passive plugin.

%package -n python2-dnf-plugins-core
Summary:    Python 2 interface to core plugins for DNF
Group:      System/Configuration/Packaging
BuildRequires:  python2-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python2-dnf < %{dnf_not_compatible}
BuildRequires:  python2-nose
BuildRequires:  python2-sphinx
BuildRequires:  python2-devel
Requires:   python2-dnf >= %{dnf_lowest_compatible}
Requires:   python2-dnf < %{dnf_not_compatible}
Requires:   python2-hawkey >= %{hawkey_version}

Provides:    python2-dnf-plugins-extras-debug = %{version}-%{release}
Provides:    python2-dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:    python2-dnf-plugins-extras-repograph = %{version}-%{release}
Provides:    python2-dnf-plugins-extras-repomanage = %{version}-%{release}
Obsoletes:   python2-dnf-plugins-extras-debug < %{dnf_plugins_extra}
Obsoletes:   python2-dnf-plugins-extras-repoclosure < %{dnf_plugins_extra}
Obsoletes:   python2-dnf-plugins-extras-repograph < %{dnf_plugins_extra}
Obsoletes:   python2-dnf-plugins-extras-repomanage < %{dnf_plugins_extra}

Conflicts:   %{name} <= 0.1.5
# let the both python plugin versions be updated simultaneously
Conflicts:   python-%{name} < %{version}-%{release}
Conflicts:   python2-%{name} < %{version}-%{release}


%description -n python2-dnf-plugins-core
Core Plugins for DNF, Python 2 interface. This package enhances DNF with
the builddep, config-manager, %{?_with_copr_plugin:copr, }debug, debuginfo-install,
download, needs-restarting, repoclosure, repograph, repomanage, and reposync commands.
Additionally, it provides the generate_completion_cache passive plugin.

%package -n python-dnf-plugins-core
Summary:    Python 3 interface to core plugins for DNF
Group:      System/Configuration/Packaging
BuildRequires:  python-devel
BuildRequires:  python-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python-dnf < %{dnf_not_compatible}
BuildRequires:  python-nose
BuildRequires:  python-sphinx
Requires:   python-dnf >= %{dnf_lowest_compatible}
Requires:   python-dnf < %{dnf_not_compatible}
Requires:   python-hawkey >= %{hawkey_version}

Conflicts:  %{name} <= 0.1.5
# let the both python plugin versions be updated simultaneously
Conflicts:  python-%{name} < %{version}-%{release}
Conflicts:  python2-%{name} < %{version}-%{release}
Provides:   python-dnf-plugins-extras-debug = %{version}-%{release}
Provides:   python-dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:   python-dnf-plugins-extras-repograph = %{version}-%{release}
Provides:   python-dnf-plugins-extras-repomanage = %{version}-%{release}
Obsoletes:  python-dnf-plugins-extras-debug < %{dnf_plugins_extra}
Obsoletes:  python-dnf-plugins-extras-repoclosure < %{dnf_plugins_extra}
Obsoletes:  python-dnf-plugins-extras-repograph < %{dnf_plugins_extra}
Obsoletes:  python-dnf-plugins-extras-repomanage < %{dnf_plugins_extra}


%description -n python-dnf-plugins-core
Core Plugins for DNF, Python 3 interface. This package enhances DNF with
the builddep, config-manager, %{?_with_copr_plugin:copr, }debug, debuginfo-install,
download, needs-restarting, repoclosure, repograph, repomanage, and reposync commands.
Additionally, it provides the generate_completion_cache passive plugin.

%package -n dnf-utils
Summary:        Yum-utils CLI compatibility layer
Group:          System/Configuration/Packaging
Conflicts:      yum-utils
# Allow GDB to have dnf-utils satisfy its requirement for debuginfo-install command
Provides:       pkg-command(debuginfo-install)
# Conflict with other provider of /usr/bin/debuginfo-install
Conflicts:      urpmi-debug-info-install
# Conflict with older versions where debuginfo-install was bundled
Conflicts:      gdb < 8.0
Requires:       dnf >= %{dnf_lowest_compatible}
Requires:       %{name} = %{version}-%{release}
%if %{with python3}
Requires:       python-dnf >= %{dnf_lowest_compatible}
Requires:       python-dnf < %{dnf_not_compatible}
%else
Requires:       python2-dnf >= %{dnf_lowest_compatible}
Requires:       python2-dnf < %{dnf_not_compatible}
%endif

%description -n dnf-utils
As a Yum-utils CLI compatibility layer, supplies in CLI shims for
debuginfo-install, repograph, package-cleanup, repoclosure, repomanage,
repoquery, reposync, repotrack, builddep, config-manager, debug, and
download that use new implementations using DNF.


%package -n python2-dnf-plugin-leaves
Summary:        Leaves Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       python2-%{name} = %{version}-%{release}
Provides:       python2-dnf-plugins-extras-leaves = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-command(leaves)
Provides:       dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugins-extras-leaves = %{version}-%{release}
%endif
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python-dnf-plugin-leaves < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-leaves < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-leaves
Leaves Plugin for DNF, Python 2 version. List all installed packages
not required by any other installed package.

%if %{with python3}
%package -n python-dnf-plugin-leaves
Summary:        Leaves Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       python-%{name} = %{version}-%{release}
Provides:       python-dnf-plugins-extras-leaves = %{version}-%{release}
Provides:       dnf-command(leaves)
Provides:       dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugins-extras-leaves = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-leaves < %{version}-%{release}
Obsoletes:      python-dnf-plugins-extras-leaves < %{dnf_plugins_extra}

%description -n python-dnf-plugin-leaves
Leaves Plugin for DNF, Python 3 version. List all installed packages
not required by any other installed package.
%endif

%package -n python2-dnf-plugin-local
Summary:        Local Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       createrepo_c
Requires:       python2-%{name} = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-local =  %{version}-%{release}
Provides:       dnf-plugins-extras-local = %{version}-%{release}
%endif
Provides:       python2-dnf-plugins-extras-local = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python-dnf-plugin-local < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-local < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-local
Local Plugin for DNF, Python 2 version. Automatically copy all downloaded packages to a
repository on the local filesystem and generating repo metadata.

%if %{with python3}
%package -n python-dnf-plugin-local
Summary:        Local Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       createrepo_c
Requires:       python-%{name} = %{version}-%{release}
Provides:       dnf-plugin-local =  %{version}-%{release}
Provides:       python-dnf-plugins-extras-local = %{version}-%{release}
Provides:       dnf-plugins-extras-local = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-local < %{version}-%{release}
Obsoletes:      python-dnf-plugins-extras-local < %{dnf_plugins_extra}

%description -n python-dnf-plugin-local
Local Plugin for DNF, Python 3 version. Automatically copy all downloaded
packages to a repository on the local filesystem and generating repo metadata.
%endif

%if %{with yum_migrate}
%package -n python2-dnf-plugin-migrate
Summary:        Migrate Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       python2-%{name} = %{version}-%{release}
Requires:       yum
Provides:       dnf-plugin-migrate = %{version}-%{release}
Provides:       python2-dnf-plugins-extras-migrate = %{version}-%{release}
Provides:       dnf-command(migrate)
Provides:       dnf-plugins-extras-migrate = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Obsoletes:      python2-dnf-plugins-extras-migrate < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-migrate
Migrate Plugin for DNF, Python 2 version. Migrates history, group and yumdb data from yum to dnf.
%endif

%package -n python2-dnf-plugin-show-leaves
Summary:        Leaves Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       python2-%{name} = %{version}-%{release}
Requires:       python2-dnf-plugin-leaves = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-show-leaves =  %{version}-%{release}
Provides:       dnf-command(show-leaves)
Provides:       dnf-plugins-extras-show-leaves = %{version}-%{release}
%endif
Provides:       python2-dnf-plugins-extras-show-leaves = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python-dnf-plugin-show-leaves < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-show-leaves < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-show-leaves
Show-leaves Plugin for DNF, Python 2 version. List all installed
packages that are no longer required by any other installed package
after a transaction.

%if %{with python3}
%package -n python-dnf-plugin-show-leaves
Summary:        Show-leaves Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       python-%{name} = %{version}-%{release}
Requires:       python-dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugin-show-leaves =  %{version}-%{release}
Provides:       python-dnf-plugins-extras-show-leaves = %{version}-%{release}
Provides:       dnf-command(show-leaves)
Provides:       dnf-plugins-extras-show-leaves = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-show-leaves < %{version}-%{release}
Obsoletes:      python-dnf-plugins-extras-show-leaves < %{dnf_plugins_extra}

%description -n python-dnf-plugin-show-leaves
Show-leaves Plugin for DNF, Python 3 version. List all installed
packages that are no longer required by any other installed package
after a transaction.
%endif

%package -n python2-dnf-plugin-versionlock
Summary:        Version Lock Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       python2-%{name} = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-versionlock =  %{version}-%{release}
Provides:       dnf-command(versionlock)
Provides:       dnf-plugins-extras-versionlock = %{version}-%{release}
%endif
Provides:       python2-dnf-plugins-extras-versionlock = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python-dnf-plugin-versionlock < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-versionlock < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-versionlock
Version lock plugin takes a set of name/versions for packages and excludes all other
versions of those packages. This allows you to e.g. protect packages from being
updated by newer versions.

%if %{with python3}
%package -n python-dnf-plugin-versionlock
Summary:        Version Lock Plugin for DNF
Group:          System/Configuration/Packaging
Requires:       python-%{name} = %{version}-%{release}
Provides:       dnf-plugin-versionlock =  %{version}-%{release}
Provides:       python-dnf-plugins-extras-versionlock = %{version}-%{release}
Provides:       dnf-command(versionlock)
Provides:       dnf-plugins-extras-versionlock = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-versionlock < %{version}-%{release}
Obsoletes:      python-dnf-plugins-extras-versionlock < %{dnf_plugins_extra}

%description -n python-dnf-plugin-versionlock
Version lock plugin takes a set of name/versions for packages and excludes all other
versions of those packages. This allows you to e.g. protect packages from being
updated by newer versions.
%endif


%prep
%autosetup -p1

%if %{with python3}
rm -rf py3
mkdir py3
%endif

%build
%cmake
%make_build
make doc-man

%if %{with python3}
# Py3 build
pushd ../py3
%cmake -DPYTHON_DESIRED:str=3 ../../
%make_build
make doc-man
popd
%endif

%install
pushd ./build
%make_install
popd
%find_lang %{name}

%if %{with python3}
# Py3 install
pushd ./py3/build
%make_install
popd
%endif

%if ! %{with yum_migrate}
rm -rf %{buildroot}%{python2_sitelib}/dnf-plugins/migrate.*
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.migrate.*
%endif

%if %{with python3}
mv %{buildroot}%{_libexecdir}/dnf-utils-3 %{buildroot}%{_libexecdir}/dnf-utils
%else
mv %{buildroot}%{_libexecdir}/dnf-utils-2 %{buildroot}%{_libexecdir}/dnf-utils
%endif
rm -vf %{buildroot}%{_libexecdir}/dnf-utils-*

mkdir -p %{buildroot}%{_bindir}
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/debuginfo-install
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/find-repos-of-install
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repo-graph
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/package-cleanup
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoclosure
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repomanage
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoquery
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/reposync
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repotrack
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-builddep
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-config-manager
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-dump
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-restore
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yumdownloader


%check
PYTHONPATH=./plugins /usr/bin/nosetests-2.* -s tests/

%if %{with python3}
# Py3 check
PYTHONPATH=./plugins /usr/bin/nosetests-3.* -s tests/
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.rst
%{_mandir}/man8/dnf.plugin.builddep.*
%{_mandir}/man8/dnf.plugin.config_manager.*
%if %{with copr_plugin}
%{_mandir}/man8/dnf.plugin.copr.*
%else
%exclude %{_mandir}/man8/dnf.plugin.copr.*
%endif
%{_mandir}/man8/dnf.plugin.debug.*
%{_mandir}/man8/dnf.plugin.debuginfo-install.*
%{_mandir}/man8/dnf.plugin.download.*
%{_mandir}/man8/dnf.plugin.generate_completion_cache.*
%{_mandir}/man8/dnf.plugin.needs_restarting.*
%{_mandir}/man8/dnf.plugin.repoclosure.*
%{_mandir}/man8/dnf.plugin.repograph.*
%{_mandir}/man8/dnf.plugin.repomanage.*
%{_mandir}/man8/dnf.plugin.reposync.*
%dir %{_sysconfdir}/dnf/protected.d
%ghost %{_var}/cache/dnf/packages.db
%config(noreplace) %{_sysconfdir}/dnf/plugins/debuginfo-install.conf

%files -n python2-dnf-plugins-core
%license COPYING
%doc AUTHORS README.rst
%{python2_sitelib}/dnf-plugins/builddep.*
%{python2_sitelib}/dnf-plugins/config_manager.*
%if %{with copr_plugin}
%{python2_sitelib}/dnf-plugins/copr.*
%else
%exclude %{python2_sitelib}/dnf-plugins/copr.*
%endif
%{python2_sitelib}/dnf-plugins/debug.*
%{python2_sitelib}/dnf-plugins/debuginfo-install.*
%{python2_sitelib}/dnf-plugins/download.*
%{python2_sitelib}/dnf-plugins/generate_completion_cache.*
%{python2_sitelib}/dnf-plugins/needs_restarting.*
%{python2_sitelib}/dnf-plugins/repoclosure.*
%{python2_sitelib}/dnf-plugins/repograph.*
%{python2_sitelib}/dnf-plugins/repomanage.*
%{python2_sitelib}/dnf-plugins/reposync.*
%{python2_sitelib}/dnfpluginscore/

%if %{with python3}
%files -n python-dnf-plugins-core
%license COPYING
%doc AUTHORS README.rst
%{python3_sitelib}/dnf-plugins/builddep.py
%{python3_sitelib}/dnf-plugins/__pycache__/builddep.*
%{python3_sitelib}/dnf-plugins/config_manager.py
%{python3_sitelib}/dnf-plugins/__pycache__/config_manager.*
%if %{with copr_plugin}
%{python3_sitelib}/dnf-plugins/copr.py
%{python3_sitelib}/dnf-plugins/__pycache__/copr.*
%else
%exclude %{python3_sitelib}/dnf-plugins/copr.*
%exclude %{python3_sitelib}/dnf-plugins/__pycache__/copr.*
%endif
%{python3_sitelib}/dnf-plugins/debug.py
%{python3_sitelib}/dnf-plugins/__pycache__/debug.*
%{python3_sitelib}/dnf-plugins/debuginfo-install.py
%{python3_sitelib}/dnf-plugins/__pycache__/debuginfo-install.*
%{python3_sitelib}/dnf-plugins/download.py
%{python3_sitelib}/dnf-plugins/__pycache__/download.*
%{python3_sitelib}/dnf-plugins/generate_completion_cache.py
%{python3_sitelib}/dnf-plugins/__pycache__/generate_completion_cache.*
%{python3_sitelib}/dnf-plugins/needs_restarting.py
%{python3_sitelib}/dnf-plugins/__pycache__/needs_restarting.*
%{python3_sitelib}/dnf-plugins/repoclosure.py
%{python3_sitelib}/dnf-plugins/__pycache__/repoclosure.*
%{python3_sitelib}/dnf-plugins/repograph.py
%{python3_sitelib}/dnf-plugins/__pycache__/repograph.*
%{python3_sitelib}/dnf-plugins/repomanage.py
%{python3_sitelib}/dnf-plugins/__pycache__/repomanage.*
%{python3_sitelib}/dnf-plugins/reposync.py
%{python3_sitelib}/dnf-plugins/__pycache__/reposync.*
%{python3_sitelib}/dnfpluginscore/
%endif

%files -n dnf-utils
%{_libexecdir}/dnf-utils
%{_bindir}/debuginfo-install
%{_bindir}/find-repos-of-install
%{_bindir}/package-cleanup
%{_bindir}/repo-graph
%{_bindir}/repoclosure
%{_bindir}/repomanage
%{_bindir}/repoquery
%{_bindir}/reposync
%{_bindir}/repotrack
%{_bindir}/yum-builddep
%{_bindir}/yum-config-manager
%{_bindir}/yum-debug-dump
%{_bindir}/yum-debug-restore
%{_bindir}/yumdownloader

%files -n python2-dnf-plugin-leaves
%{python2_sitelib}/dnf-plugins/leaves.*
%{_mandir}/man8/dnf.plugin.leaves.*

%if %{with python3}
%files -n python-dnf-plugin-leaves
%{python3_sitelib}/dnf-plugins/leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/leaves.*
%{_mandir}/man8/dnf.plugin.leaves.*
%endif

%files -n python2-dnf-plugin-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python2_sitelib}/dnf-plugins/local.*
%{_mandir}/man8/dnf.plugin.local.*

%if %{with python3}
%files -n python-dnf-plugin-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python3_sitelib}/dnf-plugins/local.*
%{python3_sitelib}/dnf-plugins/__pycache__/local.*
%{_mandir}/man8/dnf.plugin.local.*
%endif

%if %{with yum_migrate}
%files -n python2-dnf-plugin-migrate
%{python2_sitelib}/dnf-plugins/migrate.*
%{_mandir}/man8/dnf.plugin.migrate.*
%endif

%files -n python2-dnf-plugin-show-leaves
%{python2_sitelib}/dnf-plugins/show_leaves.*
%{_mandir}/man8/dnf.plugin.show-leaves.*

%if %{with python3}
%files -n python-dnf-plugin-show-leaves
%{python3_sitelib}/dnf-plugins/show_leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/show_leaves.*
%{_mandir}/man8/dnf.plugin.show-leaves.*
%endif

%files -n python2-dnf-plugin-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python2_sitelib}/dnf-plugins/versionlock.*
%{_mandir}/man8/dnf.plugin.versionlock.*

%if %{with python3}
%files -n python-dnf-plugin-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python3_sitelib}/dnf-plugins/versionlock.*
%{python3_sitelib}/dnf-plugins/__pycache__/versionlock.*
%{_mandir}/man8/dnf.plugin.versionlock.*
%endif


