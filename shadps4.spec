%global commit a9f8eaf
%global datetimever 202507181445%{commit}

Name: shadps4-git
Version: %{datetimever}
Release: %autorelease.1
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
%autochangelog

