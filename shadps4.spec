%global commit 5183cbe
%global datetimever 2025120500475183cbe

Name: shadps4-git
Version: 2025120500475183cbe
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

