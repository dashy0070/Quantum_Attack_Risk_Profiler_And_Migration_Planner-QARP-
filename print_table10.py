import docx

doc = docx.Document("2_CS_13_Capstone Project_Quantum_Attack_Risk_Profiler_And_Migration_Planner(QARP)_2026_v3.docx")

# Find table near para 481
for t in doc.tables:
    first_row = " ".join(c.text for c in t.rows[0].cells)
    if "Settlement Volume" in first_row or "TPS" in first_row or "HSM" in first_row:
        for r_idx, r in enumerate(t.rows):
            print(f"Row {r_idx}: " + " | ".join(c.text.replace("\n", " ").strip() for c in r.cells))
