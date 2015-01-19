{
    'name' : 'Modoo Live Support',
    'author': 'OpenERP SA',
    'version': '1.0',
    'summary': 'Chat with the Modoo collaborators',
    'category': 'Tools',
    'complexity': 'medium',
    'website': 'https://www.modoo.com/',
    'description':
        """
Modoo Live Support
=================

Ask your functionnal question directly to the Modoo Operators with the livechat support.

        """,
    'data': [
        "views/im_odoo_support.xml"
    ],
    'depends' : ["web", "im_chat"],
    'qweb': [
        'static/src/xml/im_odoo_support.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
