%global commit c898071
%global datetimever 202601200050c898071

Name: shadps4-git
Version: 202601200050c898071
Release: 1%{?dist}
Summary: shadPS4 is an early PlayStation 4 emulator.

License: GPL-2.0-only
URL: https://shadps4.net/

BuildRequires: clang >= 18
BuildRequires: git
BuildRequires: cmake
BuildRequires: libatomic
BuildRequires: alsa-lib-devel
BuildRequires: pipewire-jack-audio-connection-kit-devel
BuildRequires: openal-soft-devel
BuildRequires: openssl-devel
BuildRequires: libevdev-devel
BuildRequires: libudev-devel
BuildRequires: libXcursor-devel
BuildRequires: libXext-devel
BuildRequires: vulkan-devel
BuildRequires: vulkan-validation-layers
BuildRequires: libpng-devel
BuildRequires: libuuid-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: libxkbcommon-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: libdecor-devel

%description
shadPS4 is an early PlayStation 4 emulator for Windows, Linux and macOS written in C++.


%prep
git clone --recurse-submodules https://github.com/shadps4-emu/shadPS4.git %{name}-%{version}
cd %{name}-%{version}
git checkout %{commit}
git submodule update --init --recursive


%build
%cmake %{name}-%{version} -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_CXX_FLAGS="-Qunused-arguments" -DCMAKE_C_FLAGS="-Qunused-arguments"
%cmake_build


%install
%cmake_install


%check


%files
%license
%doc
%{_bindir}/shadps4

%changelog
* Tue Jan 20 2026 GitHub Actions <actions@github.com> - 202601200050c898071-1
- Auto-update to shadPS4 commit c898071

* Sun Jan 18 2026 GitHub Actions <actions@github.com> - 202601180055950d390-1
- Auto-update to shadPS4 commit 950d390

* Sat Jan 17 2026 GitHub Actions <actions@github.com> - 202601170049dce9c04-1
- Auto-update to shadPS4 commit dce9c04

* Fri Jan 16 2026 GitHub Actions <actions@github.com> - 20260116005211ee79a-1
- Auto-update to shadPS4 commit 11ee79a

* Thu Jan 15 2026 GitHub Actions <actions@github.com> - 202601150049cdf3c46-1
- Auto-update to shadPS4 commit cdf3c46

* Wed Jan 14 2026 GitHub Actions <actions@github.com> - 2026011400531a99ab7-1
- Auto-update to shadPS4 commit 1a99ab7

* Tue Jan 13 2026 GitHub Actions <actions@github.com> - 202601130046540fdcc-1
- Auto-update to shadPS4 commit 540fdcc

* Mon Jan 12 2026 GitHub Actions <actions@github.com> - 202601120054910f737-1
- Auto-update to shadPS4 commit 910f737

* Sun Jan 11 2026 GitHub Actions <actions@github.com> - 20260111005612cd27d-1
- Auto-update to shadPS4 commit 12cd27d

* Sat Jan 10 2026 GitHub Actions <actions@github.com> - 202601100049f42a566-1
- Auto-update to shadPS4 commit f42a566

* Fri Jan 09 2026 GitHub Actions <actions@github.com> - 202601090051233192f-1
- Auto-update to shadPS4 commit 233192f

* Thu Jan 08 2026 GitHub Actions <actions@github.com> - 202601080051240c1d6-1
- Auto-update to shadPS4 commit 240c1d6

* Wed Jan 07 2026 GitHub Actions <actions@github.com> - 202601070051299159b-1
- Auto-update to shadPS4 commit 299159b

* Tue Jan 06 2026 GitHub Actions <actions@github.com> - 20260106005155e2b0f-1
- Auto-update to shadPS4 commit 55e2b0f

* Mon Jan 05 2026 GitHub Actions <actions@github.com> - 202601050055256397a-1
- Auto-update to shadPS4 commit 256397a

* Wed Dec 31 2025 GitHub Actions <actions@github.com> - 202512310051954cc77-1
- Auto-update to shadPS4 commit 954cc77

* Mon Dec 29 2025 GitHub Actions <actions@github.com> - 2025122900549a3e4ea-1
- Auto-update to shadPS4 commit 9a3e4ea

* Thu Dec 25 2025 GitHub Actions <actions@github.com> - 202512250049aa227ca-1
- Auto-update to shadPS4 commit aa227ca

* Wed Dec 24 2025 GitHub Actions <actions@github.com> - 20251224004905f14e3-1
- Auto-update to shadPS4 commit 05f14e3

* Mon Dec 22 2025 GitHub Actions <actions@github.com> - 202512220052138425f-1
- Auto-update to shadPS4 commit 138425f

* Sat Dec 20 2025 GitHub Actions <actions@github.com> - 2025122000452bbb04f-1
- Auto-update to shadPS4 commit 2bbb04f

* Wed Dec 17 2025 GitHub Actions <actions@github.com> - 202512170045eae5e0a-1
- Auto-update to shadPS4 commit eae5e0a

* Sat Dec 13 2025 GitHub Actions <actions@github.com> - 2025121300459e28756-1
- Auto-update to shadPS4 commit 9e28756

* Fri Dec 12 2025 GitHub Actions <actions@github.com> - 2025121200489e7df6a-1
- Auto-update to shadPS4 commit 9e7df6a

* Tue Dec 09 2025 GitHub Actions <actions@github.com> - 202512090047de6c5bb-1
- Auto-update to shadPS4 commit de6c5bb

* Mon Dec 08 2025 GitHub Actions <actions@github.com> - 2025120800482a5910e-1
- Auto-update to shadPS4 commit 2a5910e

* Sun Dec 07 2025 GitHub Actions <actions@github.com> - 202512070053d3ad728-1
- Auto-update to shadPS4 commit d3ad728

* Fri Dec 05 2025 GitHub Actions <actions@github.com> - 2025120500475183cbe-1
- Auto-update to shadPS4 commit 5183cbe

* Thu Dec 04 2025 GitHub Actions <actions@github.com> - 20251204004798fd068-1
- Auto-update to shadPS4 commit 98fd068

* Wed Dec 03 2025 GitHub Actions <actions@github.com> - 2025120300469db4642-1
- Auto-update to shadPS4 commit 9db4642

* Tue Dec 02 2025 GitHub Actions <actions@github.com> - 202512020047a5f9280-1
- Auto-update to shadPS4 commit a5f9280

* Mon Dec 01 2025 GitHub Actions <actions@github.com> - 202512010057cf866ab-1
- Auto-update to shadPS4 commit cf866ab

* Sun Nov 30 2025 GitHub Actions <actions@github.com> - 20251130005378e301c-1
- Auto-update to shadPS4 commit 78e301c

%autochangelog

