Name:     yasm
Version:  1.3.0
Release:  1
Summary:  The Yasm Modular Assembler Project
License:  https://github.com/yasm/yasm/blob/master/BSD.txt
URL:      http://yasm.tortall.net/
Source:   http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz

%description
Yasm is a complete rewrite of the NASM assembler under the “new” BSD License (some portions are under other licenses, see COPYING for details).
Yasm currently supports the x86 and AMD64 instruction sets, accepts NASM and GAS assembler syntaxes, outputs binary, ELF32, ELF64, 32 and 64-bit Mach-O, RDOFF2, COFF, Win32, and Win64 object formats, and generates source debugging information in STABS, DWARF 2, and CodeView 8 formats.
Yasm can be easily integrated into Visual Studio 2005/2008 and 2010 for assembly of NASM or GAS syntax code into Win32 or Win64 object files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/vsyasm
%{_bindir}/yasm
%{_bindir}/ytasm
/usr/include/libyasm-stdint.h
/usr/include/libyasm.h
/usr/include/libyasm/*
%{_libdir}/libyasm.a
%{_mandir}/man1/yasm.1.gz
%{_mandir}/man7/yasm_arch.7.gz
%{_mandir}/man7/yasm_dbgfmts.7.gz
%{_mandir}/man7/yasm_objfmts.7.gz
%{_mandir}/man7/yasm_parsers.7.gz
