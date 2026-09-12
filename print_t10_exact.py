import docx

doc = docx.Document("2_CS_13_Capstone Project_Quantum_Attack_Risk_Profiler_And_Migration_Planner(QARP)_2026_v3.docx")

# Let's inspect all tables and their preceding paragraphs
for t_idx, t in enumerate(doc.tables):
    for r_idx, r in enumerate(t.rows):
        row_str = " | ".join(c.text.replace("\n", " ").strip() for c in r.cells)
        if "1,000 TPS" in row_str:
            print(f"--- Table {t_idx} ---")
            for i, r2 in enumerate(t.rows):
                print(f"Row {i}: " + " | ".join(c.text.replace("\n", " ").strip() for c in r2.cells))
            break
