%global commit 9fb948c
%global datetimever 2026062701569fb948c

Name: shadps4-git
Version: 2026062701569fb948c
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
BuildRequires: libXi-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: cxxtest

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
* Sat Jun 27 2026 GitHub Actions <actions@github.com> - 2026062701569fb948c-1
- Auto-update to shadPS4 commit 9fb948c

* Fri Jun 26 2026 GitHub Actions <actions@github.com> - 2026062602026f568ea-1
- Auto-update to shadPS4 commit 6f568ea

* Thu Jun 25 2026 GitHub Actions <actions@github.com> - 202606250200aff387e-1
- Auto-update to shadPS4 commit aff387e

* Tue Jun 23 2026 GitHub Actions <actions@github.com> - 2026062301577bb1f9d-1
- Auto-update to shadPS4 commit 7bb1f9d

* Mon Jun 22 2026 GitHub Actions <actions@github.com> - 2026062202311155575-1
- Auto-update to shadPS4 commit 1155575

* Sun Jun 21 2026 GitHub Actions <actions@github.com> - 202606210215664804b-1
- Auto-update to shadPS4 commit 664804b

* Sat Jun 20 2026 GitHub Actions <actions@github.com> - 202606200203dcd036d-1
- Auto-update to shadPS4 commit dcd036d

* Fri Jun 19 2026 GitHub Actions <actions@github.com> - 202606190243d9f68b5-1
- Auto-update to shadPS4 commit d9f68b5

* Thu Jun 18 2026 GitHub Actions <actions@github.com> - 202606180215462cd07-1
- Auto-update to shadPS4 commit 462cd07

* Wed Jun 17 2026 GitHub Actions <actions@github.com> - 202606170229bc74c60-1
- Auto-update to shadPS4 commit bc74c60

* Tue Jun 16 2026 GitHub Actions <actions@github.com> - 2026061602327de583b-1
- Auto-update to shadPS4 commit 7de583b

* Mon Jun 15 2026 GitHub Actions <actions@github.com> - 2026061502296a20eba-1
- Auto-update to shadPS4 commit 6a20eba

* Sun Jun 14 2026 GitHub Actions <actions@github.com> - 2026061402133590426-1
- Auto-update to shadPS4 commit 3590426

* Sat Jun 13 2026 GitHub Actions <actions@github.com> - 2026061302038c4e392-1
- Auto-update to shadPS4 commit 8c4e392

* Fri Jun 12 2026 GitHub Actions <actions@github.com> - 2026061202103184358-1
- Auto-update to shadPS4 commit 3184358

* Thu Jun 11 2026 GitHub Actions <actions@github.com> - 202606110214e369d8f-1
- Auto-update to shadPS4 commit e369d8f

* Wed Jun 10 2026 GitHub Actions <actions@github.com> - 202606100203d7ccf25-1
- Auto-update to shadPS4 commit d7ccf25

* Tue Jun 09 2026 GitHub Actions <actions@github.com> - 2026060901520d4fc27-1
- Auto-update to shadPS4 commit 0d4fc27

* Mon Jun 08 2026 GitHub Actions <actions@github.com> - 2026060802148525398-1
- Auto-update to shadPS4 commit 8525398

* Sun Jun 07 2026 GitHub Actions <actions@github.com> - 202606070210057454f-1
- Auto-update to shadPS4 commit 057454f

* Sat Jun 06 2026 GitHub Actions <actions@github.com> - 2026060601545b8b66a-1
- Auto-update to shadPS4 commit 5b8b66a

* Thu Jun 04 2026 GitHub Actions <actions@github.com> - 2026060402296c282aa-1
- Auto-update to shadPS4 commit 6c282aa

* Wed Jun 03 2026 GitHub Actions <actions@github.com> - 202606030232e777f56-1
- Auto-update to shadPS4 commit e777f56

* Tue Jun 02 2026 GitHub Actions <actions@github.com> - 20260602021487e774c-1
- Auto-update to shadPS4 commit 87e774c

* Mon Jun 01 2026 GitHub Actions <actions@github.com> - 2026060102132736ce8-1
- Auto-update to shadPS4 commit 2736ce8

* Sat May 30 2026 GitHub Actions <actions@github.com> - 2026053001524ce43a6-1
- Auto-update to shadPS4 commit 4ce43a6

* Fri May 29 2026 GitHub Actions <actions@github.com> - 20260529015702010ac-1
- Auto-update to shadPS4 commit 02010ac

* Thu May 28 2026 GitHub Actions <actions@github.com> - 2026052801471d885f2-1
- Auto-update to shadPS4 commit 1d885f2

* Wed May 27 2026 GitHub Actions <actions@github.com> - 20260527020378053e7-1
- Auto-update to shadPS4 commit 78053e7

* Tue May 26 2026 GitHub Actions <actions@github.com> - 2026052601550f094cb-1
- Auto-update to shadPS4 commit 0f094cb

* Mon May 25 2026 GitHub Actions <actions@github.com> - 2026052502045be4fb8-1
- Auto-update to shadPS4 commit 5be4fb8

* Sun May 24 2026 GitHub Actions <actions@github.com> - 20260524015719f2997-1
- Auto-update to shadPS4 commit 19f2997

* Fri May 22 2026 GitHub Actions <actions@github.com> - 20260522020000339cf-1
- Auto-update to shadPS4 commit 00339cf

* Thu May 21 2026 GitHub Actions <actions@github.com> - 20260521015903ebac5-1
- Auto-update to shadPS4 commit 03ebac5

* Wed May 20 2026 GitHub Actions <actions@github.com> - 2026052001596b5adca-1
- Auto-update to shadPS4 commit 6b5adca

* Tue May 19 2026 GitHub Actions <actions@github.com> - 202605190159112a456-1
- Auto-update to shadPS4 commit 112a456

* Mon May 18 2026 GitHub Actions <actions@github.com> - 202605180159caec231-1
- Auto-update to shadPS4 commit caec231

* Sun May 17 2026 GitHub Actions <actions@github.com> - 202605170150f4b787f-1
- Auto-update to shadPS4 commit f4b787f

* Sat May 16 2026 GitHub Actions <actions@github.com> - 2026051601467337364-1
- Auto-update to shadPS4 commit 7337364

* Fri May 15 2026 GitHub Actions <actions@github.com> - 20260515015285b6f5f-1
- Auto-update to shadPS4 commit 85b6f5f

* Wed May 13 2026 GitHub Actions <actions@github.com> - 2026051301520c78ea9-1
- Auto-update to shadPS4 commit 0c78ea9

* Tue May 12 2026 GitHub Actions <actions@github.com> - 20260512014789b8863-1
- Auto-update to shadPS4 commit 89b8863

* Mon May 11 2026 GitHub Actions <actions@github.com> - 2026051101521409b26-1
- Auto-update to shadPS4 commit 1409b26

* Sun May 10 2026 GitHub Actions <actions@github.com> - 202605100145d3597c7-1
- Auto-update to shadPS4 commit d3597c7

* Sat May 09 2026 GitHub Actions <actions@github.com> - 2026050901447132795-1
- Auto-update to shadPS4 commit 7132795

* Thu May 07 2026 GitHub Actions <actions@github.com> - 202605070145d85a501-1
- Auto-update to shadPS4 commit d85a501

* Wed May 06 2026 GitHub Actions <actions@github.com> - 2026050601274a55453-1
- Auto-update to shadPS4 commit 4a55453

* Tue May 05 2026 GitHub Actions <actions@github.com> - 2026050501284d3827c-1
- Auto-update to shadPS4 commit 4d3827c

* Sat May 02 2026 GitHub Actions <actions@github.com> - 202605020126ea8bed1-1
- Auto-update to shadPS4 commit ea8bed1

* Fri May 01 2026 GitHub Actions <actions@github.com> - 202605010148a3e25ef-1
- Auto-update to shadPS4 commit a3e25ef

* Thu Apr 30 2026 GitHub Actions <actions@github.com> - 2026043001466d0318a-1
- Auto-update to shadPS4 commit 6d0318a

* Wed Apr 29 2026 GitHub Actions <actions@github.com> - 2026042901467672983-1
- Auto-update to shadPS4 commit 7672983

* Tue Apr 28 2026 GitHub Actions <actions@github.com> - 202604280131d47b052-1
- Auto-update to shadPS4 commit d47b052

* Sun Apr 26 2026 GitHub Actions <actions@github.com> - 202604260123a762f70-1
- Auto-update to shadPS4 commit a762f70

* Sat Apr 25 2026 GitHub Actions <actions@github.com> - 202604250114737d23b-1
- Auto-update to shadPS4 commit 737d23b

* Fri Apr 24 2026 GitHub Actions <actions@github.com> - 202604240121e455a2f-1
- Auto-update to shadPS4 commit e455a2f

* Thu Apr 23 2026 GitHub Actions <actions@github.com> - 20260423012107a0475-1
- Auto-update to shadPS4 commit 07a0475

* Wed Apr 22 2026 GitHub Actions <actions@github.com> - 2026042201162b7d54f-1
- Auto-update to shadPS4 commit 2b7d54f

* Tue Apr 21 2026 GitHub Actions <actions@github.com> - 202604210118dcdbd17-1
- Auto-update to shadPS4 commit dcdbd17

* Mon Apr 20 2026 GitHub Actions <actions@github.com> - 20260420012090b75ea-1
- Auto-update to shadPS4 commit 90b75ea

* Sun Apr 19 2026 GitHub Actions <actions@github.com> - 202604190120854b291-1
- Auto-update to shadPS4 commit 854b291

* Fri Apr 17 2026 GitHub Actions <actions@github.com> - 2026041701182d559a4-1
- Auto-update to shadPS4 commit 2d559a4

* Thu Apr 16 2026 GitHub Actions <actions@github.com> - 202604160120be224a4-1
- Auto-update to shadPS4 commit be224a4

* Wed Apr 15 2026 GitHub Actions <actions@github.com> - 202604150116c1e496e-1
- Auto-update to shadPS4 commit c1e496e

* Mon Apr 13 2026 GitHub Actions <actions@github.com> - 202604130119cead66d-1
- Auto-update to shadPS4 commit cead66d

* Sat Apr 11 2026 GitHub Actions <actions@github.com> - 2026041101095f09632-1
- Auto-update to shadPS4 commit 5f09632

* Fri Apr 10 2026 GitHub Actions <actions@github.com> - 202604100114e16a59b-1
- Auto-update to shadPS4 commit e16a59b

* Thu Apr 09 2026 GitHub Actions <actions@github.com> - 20260409010336e11fc-1
- Auto-update to shadPS4 commit 36e11fc

* Wed Apr 08 2026 GitHub Actions <actions@github.com> - 202604080113e64f038-1
- Auto-update to shadPS4 commit e64f038

* Mon Apr 06 2026 GitHub Actions <actions@github.com> - 20260406011413da5a8-1
- Auto-update to shadPS4 commit 13da5a8

* Sun Apr 05 2026 GitHub Actions <actions@github.com> - 202604050114162cb18-1
- Auto-update to shadPS4 commit 162cb18

* Fri Apr 03 2026 GitHub Actions <actions@github.com> - 20260403011126e2689-1
- Auto-update to shadPS4 commit 26e2689

* Thu Apr 02 2026 GitHub Actions <actions@github.com> - 202604020109deb8c66-1
- Auto-update to shadPS4 commit deb8c66

* Tue Mar 31 2026 GitHub Actions <actions@github.com> - 202603310112969955b-1
- Auto-update to shadPS4 commit 969955b

* Mon Mar 30 2026 GitHub Actions <actions@github.com> - 2026033001142334981-1
- Auto-update to shadPS4 commit 2334981

* Sun Mar 29 2026 GitHub Actions <actions@github.com> - 2026032901131018660-1
- Auto-update to shadPS4 commit 1018660

* Sat Mar 28 2026 GitHub Actions <actions@github.com> - 202603280104df32a20-1
- Auto-update to shadPS4 commit df32a20

* Fri Mar 27 2026 GitHub Actions <actions@github.com> - 202603270110e0a86dc-1
- Auto-update to shadPS4 commit e0a86dc

* Thu Mar 26 2026 GitHub Actions <actions@github.com> - 20260326011031b2d9c-1
- Auto-update to shadPS4 commit 31b2d9c

* Wed Mar 25 2026 GitHub Actions <actions@github.com> - 202603250105bb9c223-1
- Auto-update to shadPS4 commit bb9c223

* Tue Mar 24 2026 GitHub Actions <actions@github.com> - 202603240100f450405-1
- Auto-update to shadPS4 commit f450405

* Mon Mar 23 2026 GitHub Actions <actions@github.com> - 202603230107edd50ab-1
- Auto-update to shadPS4 commit edd50ab

* Sun Mar 22 2026 GitHub Actions <actions@github.com> - 202603220106060703f-1
- Auto-update to shadPS4 commit 060703f

* Sat Mar 21 2026 GitHub Actions <actions@github.com> - 2026032100582bb20e4-1
- Auto-update to shadPS4 commit 2bb20e4

* Fri Mar 20 2026 GitHub Actions <actions@github.com> - 2026032001020c3fac6-1
- Auto-update to shadPS4 commit 0c3fac6

* Thu Mar 19 2026 GitHub Actions <actions@github.com> - 202603190106f245cf7-1
- Auto-update to shadPS4 commit f245cf7

* Wed Mar 18 2026 GitHub Actions <actions@github.com> - 2026031801066e843d0-1
- Auto-update to shadPS4 commit 6e843d0

* Sun Mar 15 2026 GitHub Actions <actions@github.com> - 20260315011130ff9cf-1
- Auto-update to shadPS4 commit 30ff9cf

* Sat Mar 14 2026 GitHub Actions <actions@github.com> - 202603140100f336096-1
- Auto-update to shadPS4 commit f336096

* Fri Mar 13 2026 GitHub Actions <actions@github.com> - 20260313010167ffd03-1
- Auto-update to shadPS4 commit 67ffd03

* Wed Mar 11 2026 GitHub Actions <actions@github.com> - 202603110058ac3786f-1
- Auto-update to shadPS4 commit ac3786f

* Tue Mar 10 2026 GitHub Actions <actions@github.com> - 20260310005885476e5-1
- Auto-update to shadPS4 commit 85476e5

* Mon Mar 09 2026 GitHub Actions <actions@github.com> - 202603090102cc6af03-1
- Auto-update to shadPS4 commit cc6af03

* Sun Mar 08 2026 GitHub Actions <actions@github.com> - 202603080102014b11e-1
- Auto-update to shadPS4 commit 014b11e

* Fri Mar 06 2026 GitHub Actions <actions@github.com> - 20260306010789e7482-1
- Auto-update to shadPS4 commit 89e7482

* Wed Mar 04 2026 GitHub Actions <actions@github.com> - 20260304010014450d3-1
- Auto-update to shadPS4 commit 14450d3

* Tue Mar 03 2026 GitHub Actions <actions@github.com> - 2026030301041f5430e-1
- Auto-update to shadPS4 commit 1f5430e

* Mon Mar 02 2026 GitHub Actions <actions@github.com> - 202603020102e5d7dc4-1
- Auto-update to shadPS4 commit e5d7dc4

* Sun Mar 01 2026 GitHub Actions <actions@github.com> - 2026030101086a8c50c-1
- Auto-update to shadPS4 commit 6a8c50c

* Sat Feb 28 2026 GitHub Actions <actions@github.com> - 2026022800558bb2969-1
- Auto-update to shadPS4 commit 8bb2969

* Fri Feb 27 2026 GitHub Actions <actions@github.com> - 20260227010119d2027-1
- Auto-update to shadPS4 commit 19d2027

* Wed Feb 25 2026 GitHub Actions <actions@github.com> - 202602250107e1ecd8e-1
- Auto-update to shadPS4 commit e1ecd8e

* Tue Feb 24 2026 GitHub Actions <actions@github.com> - 202602240101407d287-1
- Auto-update to shadPS4 commit 407d287

* Mon Feb 23 2026 GitHub Actions <actions@github.com> - 2026022301036cbab87-1
- Auto-update to shadPS4 commit 6cbab87

* Sun Feb 22 2026 GitHub Actions <actions@github.com> - 2026022201039241ebd-1
- Auto-update to shadPS4 commit 9241ebd

* Fri Feb 20 2026 GitHub Actions <actions@github.com> - 20260220010006b901a-1
- Auto-update to shadPS4 commit 06b901a

* Wed Feb 18 2026 GitHub Actions <actions@github.com> - 202602180105a99c814-1
- Auto-update to shadPS4 commit a99c814

* Tue Feb 17 2026 GitHub Actions <actions@github.com> - 2026021701033a99051-1
- Auto-update to shadPS4 commit 3a99051

* Mon Feb 16 2026 GitHub Actions <actions@github.com> - 2026021601044a37051-1
- Auto-update to shadPS4 commit 4a37051

* Sun Feb 15 2026 GitHub Actions <actions@github.com> - 2026021501060f92285-1
- Auto-update to shadPS4 commit 0f92285

* Sat Feb 14 2026 GitHub Actions <actions@github.com> - 202602140100e0850d5-1
- Auto-update to shadPS4 commit e0850d5

* Fri Feb 13 2026 GitHub Actions <actions@github.com> - 202602130108cdafdb7-1
- Auto-update to shadPS4 commit cdafdb7

* Thu Feb 12 2026 GitHub Actions <actions@github.com> - 2026021201040435ada-1
- Auto-update to shadPS4 commit 0435ada

* Wed Feb 11 2026 GitHub Actions <actions@github.com> - 20260211011199661aa-1
- Auto-update to shadPS4 commit 99661aa

* Tue Feb 10 2026 GitHub Actions <actions@github.com> - 202602100114a706b32-1
- Auto-update to shadPS4 commit a706b32

* Mon Feb 09 2026 GitHub Actions <actions@github.com> - 202602090105afc9893-1
- Auto-update to shadPS4 commit afc9893

* Sun Feb 08 2026 GitHub Actions <actions@github.com> - 202602080120341de9a-1
- Auto-update to shadPS4 commit 341de9a

* Fri Feb 06 2026 GitHub Actions <actions@github.com> - 202602060059b88ec48-1
- Auto-update to shadPS4 commit b88ec48

* Thu Feb 05 2026 GitHub Actions <actions@github.com> - 202602050101923d1b1-1
- Auto-update to shadPS4 commit 923d1b1

* Wed Feb 04 2026 GitHub Actions <actions@github.com> - 202602040058b435731-1
- Auto-update to shadPS4 commit b435731

* Tue Feb 03 2026 GitHub Actions <actions@github.com> - 202602030103e2f3a0f-1
- Auto-update to shadPS4 commit e2f3a0f

* Sun Feb 01 2026 GitHub Actions <actions@github.com> - 2026020101103bd6a0f-1
- Auto-update to shadPS4 commit 3bd6a0f

* Sat Jan 31 2026 GitHub Actions <actions@github.com> - 202601310057c0987ec-1
- Auto-update to shadPS4 commit c0987ec

* Fri Jan 30 2026 GitHub Actions <actions@github.com> - 2026013000594f3aabd-1
- Auto-update to shadPS4 commit 4f3aabd

* Thu Jan 29 2026 GitHub Actions <actions@github.com> - 202601290059f14bad7-1
- Auto-update to shadPS4 commit f14bad7

* Wed Jan 28 2026 GitHub Actions <actions@github.com> - 202601280052c81ebe6-1
- Auto-update to shadPS4 commit c81ebe6

* Tue Jan 27 2026 GitHub Actions <actions@github.com> - 2026012700551e99c4b-1
- Auto-update to shadPS4 commit 1e99c4b

* Sun Jan 25 2026 GitHub Actions <actions@github.com> - 202601250057fa497f6-1
- Auto-update to shadPS4 commit fa497f6

* Sat Jan 24 2026 GitHub Actions <actions@github.com> - 20260124004946a7c4e-1
- Auto-update to shadPS4 commit 46a7c4e

* Fri Jan 23 2026 GitHub Actions <actions@github.com> - 202601230052fecfbb6-1
- Auto-update to shadPS4 commit fecfbb6

* Thu Jan 22 2026 GitHub Actions <actions@github.com> - 2026012200510d5c5f8-1
- Auto-update to shadPS4 commit 0d5c5f8

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

