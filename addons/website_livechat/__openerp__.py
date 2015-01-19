{
    'name': 'Website Live Support',
    'category': 'Website',
    'summary': 'Chat With Your Website Visitors',
    'version': '1.0',
    'description': """
Modoo Website LiveChat
========================
For website built with Modoo CMS, this module include a chat button on your Website, and allow your visitors to chat with your collabarators.
        """,
    'author': 'OpenERP SA',
    'depends': ['website', 'im_livechat'],
    'installable': True,
    'data': [
        'views/website_livechat.xml',
        'views/res_config.xml',
        'website_livechat_data.xml'
    ],
}
