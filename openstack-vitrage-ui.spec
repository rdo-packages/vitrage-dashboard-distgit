%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%global pypi_name vitrage-dashboard
%global mod_name  vitrage_dashboard

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

Name:           openstack-vitrage-ui
Version:        XXX
Release:        XXX
Summary:        Vitrage Management Dashboard

# bundled libraries:
# d3 is BSD licensed
# loadsh is MIT licensed
# graphlib is MIT licensed
# dagre is MIT licensed
License:        ASL 2.0 and BSD and MIT

URL:            https://github.com/openstack/vitrage-dashboard
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  git-core
BuildRequires:  openstack-macros

Requires: openstack-dashboard >= 1:17.1.0

Requires: python3-iso8601
Requires: python3-vitrageclient >= 2.5.0
Requires: python3-django-compressor >= 2.0
Requires: python3-pbr >= 2.0.0
Requires: python3-XStatic-Angular-Bootstrap >= 2.2.0.0
Requires: python3-XStatic-Angular >= 1.5.8.0
Requires: python3-XStatic-Bootstrap-SCSS >= 3.3.7.1
Requires: python3-XStatic-Font-Awesome >= 4.7.0.0
Requires: python3-XStatic-smart-table >= 1.4.13.2
Requires: python3-XStatic-D3 >= 3.5.17.0

# Not packaged in RDO https://review.rdoproject.org/r/#/c/27219/
# Requires: python3-XStatic-Dagre-D3 >= 0.4.17.0
# Requires: python3-XStatic-Dagre >= 0.6.4.0
# Requires: python3-XStatic-Graphlib >= 2.1.7.0
# Requires: python3-XStatic-lodash >= 4.16.4.1
# Requires: python3-XStatic-Moment-Timezone >= 0.5.22.0
# Requires: python3-XStatic-moment >= 2.8.4.1

Requires: python3-XStatic-Bootstrap-Datepicker >= 1.3.1.0
Requires: python3-XStatic-jQuery >= 1.8.2.1

%description
Vitrage Management Dashboard


%if 0%{?with_doc}
%package doc
Summary: Documentation for Vitrage dashboard

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-rsvgconverter

%description doc

Documentation files for OpenStack Vitrage dashboard for Horizon
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Remove bundled egg-info
%py_req_cleanup

%build
%{py3_build}

%if 0%{?with_doc}
# Build html documentation
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%{py3_install}

# Move config to horizon
mkdir -p  %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled
mkdir -p  %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled

mv vitrage_dashboard/enabled/_4*.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/

ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4000_project_vitrage_panel_group.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4000_project_vitrage_panel_group.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4010_project_topology_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4010_project_topology_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4020_project_alarms_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4020_project_alarms_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4030_project_entities_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4030_project_entities_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4040_project_template_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4040_project_template_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4100_admin_vitrage_panel_group.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4100_admin_vitrage_panel_group.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4110_admin_topology_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4110_admin_topology_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4120_admin_alarms_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4120_admin_alarms_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4130_admin_entities_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4130_admin_entities_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4140_admin_template_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4140_admin_template_vitrage_panel.py


%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{mod_name}
%{python3_sitelib}/*.egg-info

%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4000_project_vitrage_panel_group.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4010_project_topology_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4020_project_alarms_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4030_project_entities_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4040_project_template_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4100_admin_vitrage_panel_group.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4110_admin_topology_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4120_admin_alarms_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4130_admin_entities_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4140_admin_template_vitrage_panel.py*

%{_sysconfdir}/openstack-dashboard/enabled/_4000_project_vitrage_panel_group.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4010_project_topology_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4020_project_alarms_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4030_project_entities_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4040_project_template_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4100_admin_vitrage_panel_group.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4110_admin_topology_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4120_admin_alarms_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4130_admin_entities_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4140_admin_template_vitrage_panel.py*

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
