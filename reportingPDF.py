from datetime import datetime
import streamlit as st
from fpdf import FPDF
import base64


def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.title
    pdf.cell(40, 10, "report_text")
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
    st.markdown(html, unsafe_allow_html=True)



class PDF(FPDF):
    def header(self):
        # Add header information
        # self.set_fill_color(192, 192, 192)  # Set gray background color
        self.set_y(4)
        self.set_font("Arial", "B", size=11.2)  # Reduce font size by 40%
        self.image("images/logo.png", x=10, y=1, w=60, h=18)  # Add image to the left
        self.cell(195, 10, "Call Report - Corporate Banking Group", 0, 0, "R", fill=False)  # Align to the right

        self.ln(16)

    def footer(self):
            # Add footer information
            self.set_y(-15)
            self.set_font("Arial", "I", size=7.8)  # Reduce font size by 40%
            self.cell(0, 10, f"Print Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 0, "C")

    def add_section_header(self, header_text):
        # Add section header
        self.set_fill_color(192, 192, 192)  # Set gray background color
        self.set_font("Arial", "B", size=8.8)  # Reduce font size by 40%
        self.set_x(10)  # Set the left margin to 10 units
        self.cell(0, 10, header_text, 0, 1, "L", fill=True)  # Align to the left and fill the cell with the background color
        # self.ln(5)

    def add_field(self, field_label, field_value):
        # Add field
        self.set_font("Arial", 'B' ,size=8.4)  # Reduce font size by 40%
        self.cell(40, 7, field_label + ":", 0, 0)
        self.set_font("Arial", size=8.4)  # Reduce font size by 40%
        self.cell(0, 7, field_value, 0, 1)

    def add_table(self, title, data):
        # Add table with title and data
        self.add_section_header(title)
        self.set_fill_color(255, 255, 204)
        self.set_font("Arial", size=6.72)  # Reduce font size by 40%
        self.cell(95, 5, "Name", 1, 0, "L", fill=True)
        self.cell(95, 5, "Designation", 1, 1, "L", fill=True)
        for person in data:
            self.cell(95, 5, person[0], 1, 0, "L")
            self.cell(95, 5, person[1], 1, 1, "L")
        self.ln(5)

    def add_report_details(self, date, department):
        # Add report details section
        self.add_section_header("Report Details")
        self.add_field("Date", date)
        self.add_field("Department", department)
        # self.ln(10)

    def add_client_details(self, client_name, client_type, referred_by):
        # Add client details section
        self.add_section_header("Client Details")
        self.add_field("Client Name", client_name)
        self.add_field("Type", client_type)
        self.add_field("Referred by", referred_by)
        # self.ln(10)

    def add_call_details(self, call_date, venue):
        # Add call details section
        self.add_section_header("Call Details")
        self.add_field("Date", call_date)
        self.add_field("Venue", venue)
        # self.ln(10)

    def add_objectives(self, objectives):
        # Add objectives section
        self.add_section_header("Objectives of the Call")
        self.set_font("Arial", size=8.4)
        self.multi_cell(0, 5, objectives)
        # self.ln(10)

    def add_discussion_points(self, points):
        # Add points of discussion section
        self.add_section_header("Points of Discussion")
        self.set_font("Arial", size=8.4)
        self.multi_cell(0, 5, points)
        # self.ln(10)

    def add_actionable_items(self, items):
        # Add actionable items section
        self.add_section_header("Actionable Items")
        self.set_font("Arial", size=8.4)
        self.multi_cell(0, 5, items)
        # self.ln(10)

    def generate_report(self, objects):
        # Set up document
        self.set_font("Arial", size=8)  # Reduce font size by 40%

        for obj in objects:
            date = obj['date']
            department = obj['department']
            client_name = obj['client_name']
            client_type = obj['client_type']
            referred_by = obj['referred_by']
            call_date = obj['call_date']
            venue = obj['venue']
            called_on_list = obj['called_on_list']
            calling_on_list = obj['calling_on_list']
            objectives = obj['objectives']
            discussion_points = obj['discussion_points']
            actionable_items = obj['actionable_items']

            # Add report details
            self.add_page()
            self.add_report_details(date, department)

            # Add client details
            self.add_client_details(client_name, client_type, referred_by)

            # Add call details
            self.add_call_details(call_date, venue)

            # Add called on list table
            self.add_table("Called on List", called_on_list)

            # Add calling on list table
            self.add_table("Calling on List", calling_on_list)

            # Add objectives
            self.add_objectives(objectives)

            # Add points of discussion
            self.add_discussion_points(discussion_points)

            # Add actionable items
            self.add_actionable_items(actionable_items)

        # Output the PDF
        # self.output("report.pdf")
        html = create_download_link(self.output(dest="S").encode("latin-1"), "test")
        return html

# Create an instance of the PDF class

# Example usage
objects = [
    {
        'date': "2023-06-01",
        'department': "Sales",
        'client_name': "John Doe",
        'client_type': "VIP",
        'referred_by': "Jane Smith",
        'call_date': "2023-06-02",
        'venue': "Conference Room",
        'called_on_list': [
            ("Person 1", "Manager"),
            ("Person 2", "Executive"),
            ("Person 3", "Associate")
        ],
        'calling_on_list': [
            ("Person 4", "Director"),
            ("Person 5", "Manager"),
            ("Person 6", "Executive")
        ],
        'objectives': "Discuss new product launch",
        'discussion_points': "Sales projections, marketing strategy, Sales projections, marketing strategy",
        'actionable_items': "Follow up on leads, schedule follow-up meeting"
    },
    {
        'date': "2023-06-02",
        'department': "Marketing",
        'client_name': "Jane Smith",
        'client_type': "Regular",
        'referred_by': "John Doe",
        'call_date': "2023-06-03",
        'venue': "Meeting Room",
        'called_on_list': [
            ("Person 7", "Manager"),
            ("Person 8", "Executive"),
            ("Person 9", "Associate")
        ],
        'calling_on_list': [
            ("Person 10", "Director"),
            ("Person 11", "Manager"),
            ("Person 12", "Executive")
        ],
        'objectives': "Discuss marketing campaign",
        'discussion_points': "Budget allocation, target audience",
        'actionable_items': "Create campaign strategy, allocate resources"
    }
]




# def export_reports_to_PDF(reports):
#     pdf = PDF()
    # pdf.generate_report(objects)





