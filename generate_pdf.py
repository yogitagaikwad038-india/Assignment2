from fpdf import FPDF
import os

os.makedirs("data", exist_ok=True)

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)

content = """
AI Product Whitepaper

The company confirms that the AI Product launch
is scheduled for June 15, 2026.

The project remains active and fully funded.

No plans exist to cancel development.

Claims circulating on social media are false.

Official statement:

The AI platform successfully passed all testing
milestones and remains on track for release.
"""

pdf.multi_cell(0, 10, content)

pdf.output("data/whitepaper.pdf")

print("✅ whitepaper.pdf created successfully")