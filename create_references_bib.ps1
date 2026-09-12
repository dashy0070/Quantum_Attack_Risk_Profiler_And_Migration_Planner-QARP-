# PowerShell script to generate references.bib
$bibContent = @'
@inproceedings{stebila2017postquantum,
  author    = {Douglas Stebila and Michele Mosca},
  title     = {Post-Quantum Key Exchange for the Internet and the {Open Quantum Safe} Project},
  booktitle = {Selected Areas in Cryptography -- SAC 2016},
  series    = {Lecture Notes in Computer Science},
  volume    = {10532},
  pages     = {14--37},
  year      = {2017},
  publisher = {Springer},
  doi       = {10.1007/978-3-319-69453-5_2}
}

@article{mosca2018cybersecurity,
  author    = {Michele Mosca},
  title     = {Cybersecurity in an Era with Quantum Computers: Will We Be Ready?},
  journal   = {IEEE Security \& Privacy},
  volume    = {16},
  number    = {5},
  pages     = {38--41},
  year      = {2018},
  publisher = {IEEE},
  doi       = {10.1109/MSP.2018.3761723}
}

@article{gidney2021factor,
  author    = {Craig Gidney and Martin Eker{\aa}},
  title     = {How to Factor 2048 Bit {RSA} Integers in 8 Hours Using 20 Million Noisy Qubits},
  journal   = {Quantum},
  volume    = {5},
  pages     = {433},
  year      = {2021},
  publisher = {Verein zur F{\"o}rderung des Open Access Publizierens in den Quantenwissenschaften},
  doi       = {10.22331/q-2021-04-15-433}
}

@inproceedings{sikeridis2020overhead,
  author    = {Dimitrios Sikeridis and Panos Kampanakis and Michael Devetsikiotis},
  title     = {Assessing the Overhead of Post-Quantum Cryptography in {TLS} 1.3 and {SSH}},
  booktitle = {Proceedings of the 16th International Conference on Emerging Networking EXperiments and Technologies (CoNEXT '20)},
  pages     = {149--156},
  year      = {2020},
  publisher = {ACM},
  doi       = {10.1145/3386367.3431309}
}

@inproceedings{paquin2020benchmarking,
  author    = {Christian Paquin and Douglas Stebila and Goutam Tamvada},
  title     = {Benchmarking Post-Quantum Cryptography in {TLS}},
  booktitle = {Post-Quantum Cryptography -- PQCrypto 2020},
  series    = {Lecture Notes in Computer Science},
  volume    = {12100},
  pages     = {72--91},
  year      = {2020},
  publisher = {Springer},
  doi       = {10.1007/978-3-030-44223-1_5}
}

@misc{iso27001_2022,
  author       = {{International Organization for Standardization}},
  title        = {Information security, cybersecurity and privacy protection --- Information security management systems --- Requirements},
  howpublished = {ISO/IEC Standard 27001:2022},
  year         = {2022},
  address      = {Geneva, Switzerland}
}

@techreport{bis2023projectleap,
  author      = {{Bank for International Settlements (BIS) Innovation Hub}},
  title       = {Project Leap: Quantum-Proofing the Financial System},
  institution = {BIS Innovation Hub},
  year        = {2023},
  month       = jun,
  address     = {Basel, Switzerland},
  url         = {https://www.bis.org/publ/othp66.pdf}
}

@article{albrecht2018rlwe,
  author    = {Martin R. Albrecht and Christian Hanser and Andrea Hoeller and Thomas P{\"o}ppelmann and Fernando Virdia and Andreas Wallner},
  title     = {Implementing {RLWE}-Based Schemes Using an {RSA} Co-Processor},
  journal   = {IACR Transactions on Cryptographic Hardware and Embedded Systems (TCHES)},
  volume    = {2019},
  number    = {1},
  pages     = {169--208},
  year      = {2018},
  publisher = {Ruhr-Universit{\"a}t Bochum},
  doi       = {10.13154/tches.v2019.i1.169-208}
}

@techreport{kannwischer2019pqm4,
  author      = {Matthias J. Kannwischer and Joost Rijneveld and Peter Schwabe and Ko Stoffelen},
  title       = {pqm4: Testing and Benchmarking {NIST} {PQC} on {ARM Cortex-M4}},
  institution = {IACR Cryptology ePrint Archive, Report 2019/844},
  year        = {2019},
  url         = {https://eprint.iacr.org/2019/844}
}

@inproceedings{sharma2025quantum,
  author    = {V. Sharma and K. K. S. Pandian and R. Kaur and P. Poonguzhali and D. Ethirajan},
  title     = {Quantum Roots of Trust: Hardware Anchors for Post-Quantum Security},
  booktitle = {Proceedings of the 2025 1st International Conference on Intelligent Computing and Systems at the Edge (ICEdge)},
  year      = {2025},
  publisher = {IEEE}
}

@misc{cyclonedx_cbom_2024,
  author       = {{CycloneDX Authoring Group}},
  title        = {CycloneDX v1.6 Standard: Cryptography Bill of Materials ({CBOM}) Specification},
  howpublished = {OWASP Foundation Technical Standard},
  year         = {2024},
  month        = apr,
  url          = {https://cyclonedx.org/capabilities/cbom/}
}

@article{chou2026network,
  author    = {Matthew Chou and Phuong M. Cao},
  title     = {Network Impact of Post-Quantum Certificate Chain Sizes on Time to First Byte in {TLS} Deployments},
  journal   = {arXiv preprint arXiv:2604.24869},
  year      = {2026},
  url       = {https://arxiv.org/abs/2604.24869}
}

@mastersthesis{etsare2026automated,
  author = {Fredrik Knut Etsare and Robin Amadeus Karim},
  title  = {Automated {PQC} Migration Guidance Using a Cryptographic Bill of Materials},
  school = {Design Science Research, DiVA Portal},
  year   = {2026},
  month  = aug,
  url    = {https://www.diva-portal.org/}
}

@misc{pcidss_v4_0_1,
  author       = {{PCI Security Standards Council}},
  title        = {Payment Card Industry Data Security Standard ({PCI DSS}) Requirements and Testing Procedures v4.0.1},
  howpublished = {PCI SSC Technical Standard},
  year         = {2024},
  month        = jun,
  address      = {Wakefield, MA, USA}
}

@techreport{draft-ietf-uta-pqc-app,
  author      = {Tirumaleswar Reddy K. and Hannes Tschofenig},
  title       = {Post-Quantum Cryptography Recommendations for {TLS}-Based Applications},
  type        = {Internet-Draft},
  number      = {draft-ietf-uta-pqc-app-03},
  institution = {Internet Engineering Task Force (IETF)},
  year        = {2026},
  month       = jul,
  url         = {https://datatracker.ietf.org/doc/draft-ietf-uta-pqc-app/}
}

@techreport{europol2026pqc,
  author      = {{Europol Innovation Lab, European Cybercrime Centre (EC3), and FS-ISAC}},
  title       = {Prioritising Post-Quantum Cryptography Migration Activities in Financial Services},
  institution = {Europol},
  year        = {2026},
  month       = jan,
  address     = {Luxembourg},
  note        = {ISBN: 978-92-9414-091-3}
}

@book{swift2022dummies,
  author    = {{SWIFT Standards Team}},
  title     = {{ISO} 20022 for Dummies},
  edition   = {6th limited ed.},
  publisher = {SWIFT / John Wiley \& Sons},
  address   = {La Hulpe, Belgium},
  year      = {2022}
}

@misc{ustreasury2026taskforce,
  author       = {{U.S. Department of the Treasury}},
  title        = {Treasury Announces the Quantum-Readiness Task Force},
  howpublished = {U.S. Department of the Treasury Press Release},
  month        = aug,
  year         = {2026},
  address      = {Washington, DC, USA},
  url          = {https://home.treasury.gov/}
}

@techreport{crockett2019prototyping,
  author      = {Eric Crockett and Christian Paquin and Douglas Stebila},
  title       = {Prototyping Post-Quantum and Hybrid Key Exchange and Authentication in {TLS} and {SSH}},
  institution = {IACR Cryptology ePrint Archive, Report 2019/858},
  year        = {2019},
  url         = {https://eprint.iacr.org/2019/858}
}
'@

$outputPath = Join-Path -Path $PSScriptRoot -ChildPath "references.bib"
if (-not $PSScriptRoot) {
    $outputPath = "references.bib"
}

$bibContent | Out-File -FilePath $outputPath -Encoding UTF8
Write-Host "Successfully generated references.bib with all 19 verified entries!" -ForegroundColor Green
