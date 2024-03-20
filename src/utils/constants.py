import os
#token constants
SECRET_KEY="5123415"

# Database constants
SQLALCHEMY_DATABASE_URL = "mysql://root:1234@localhost/hca2"

# excel_file_path contants
mock_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'mock', 'excel_data')

jobMockTablePath = os.path.join(mock_folder, 'job_table.xlsx')
formMockTablePath = os.path.join(mock_folder,'form_table.xlsx')
csatResourceMockTablePath = os.path.join(mock_folder, 'csat_resources_table.xlsx')
csatResourceFeedbackMockTablePath = os.path.join(mock_folder, 'csat_resources_feedback_table.xlsx')
formLineItemOptionsMockTablePath = os.path.join(mock_folder, 'form_line_item_options_table.xlsx')
formLineItemMockTablePath = os.path.join(mock_folder, 'form_line_items_table.xlsx')
# smtp_server constants
SMTP_PORT=587
SMTP_SERVER='smtp.gmail.com'
MAIL_LINK='http://localhost:4200/'

