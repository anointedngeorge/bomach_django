



APPLIST = [

    {'heading':'Dashboard','index':0, 'is_active':False, 'url':'',  'has_model_dropdown':False, 'icon':'fa fa-home', 'models':[
            {'title':'View Vendor', 'url':'authuser/vendor/', 'is_active':True},
            {'title':'', 'url':'', 'is_active':True},
        ],
    },
    
    {'heading':'Vendors','index':1, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-user', 'models':[
        {'title':'View Vendor', 'url':'authuser/vendor/', 'is_active':True},
        {'title':'', 'url':'', 'is_active':True},
    ],
    },

    {'heading':'Users','index':2, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-user-plus', 'models':[
        {'title':'View Users', 'url':'authuser/client/', 'is_active':True},
        {'title':'', 'url':'', 'is_active':True},
    ],
    },

    {'heading':'Human Resource','index':2, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-users', 'models':[
        {'title':'State Coordinators', 'url':'', 'is_active':True},
        {'title':'CRM / Agents', 'url':'authuser/agent/', 'is_active':True},
        {'title':'Riders', 'url':'authuser/driver/', 'is_active':True},
        {'title':'Maintance Officer', 'url':'', 'is_active':True},
    ],
    },


    {'heading':'Asset / Equipment','index':4, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-gear', 'models':[
        {'title':'Register Bike', 'url':'assetsAndEquipment/motocycle/', 'is_active':True},
        # {'title':'List Assets', 'url':'assetsAndEquipment/assignmotocycletorider/', 'is_active':True},
        # {'title':'List Vendors', 'url':'', 'is_active':True}
    ],
    },
    
    {'heading':'Work / Earnings','index':5, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-building', 'models':[
            {'title':"Rider's Earnings", 'url':'payments/commisionearneddriver/', 'is_active':True},
            {'title':"Agent Earnings", 'url':'payments/commisionearnedagents/', 'is_active':True},
        ],
    },

    {'heading':'Payrolls','index':6, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-bank', 'models':[
        {'title':'Add Payment', 'url':'', 'is_active':True},
        {'title':'List Vendors', 'url':'', 'is_active':True}
    ],
    },

    {'heading':'Ticket & Reports','index':7, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-ticket', 'models':[
        {'title':'Reports', 'url':'reports/customreports/', 'is_active':True},
        {'title':'Tickets', 'url':'tickets/tickets/', 'is_active':True}
    ],
    },

    {'heading':'Company','index':8, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-building', 'models':[
        {'title':'Add Payment', 'url':'', 'is_active':True},
        {'title':'Profile', 'url':'', 'is_active':True}
    ],
    },

    {'heading':'Finance','index':9, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-money', 'models':[
            {'title':'Agent Wallet', 'url':'', 'is_active':True},
            {'title':'Rider Wallet', 'url':'', 'is_active':True},
            {'title':'Vendor Wallet', 'url':'', 'is_active':True},
        ],
    },

     {'heading':'Settings','index':5, 'is_active':True, 'url':'',  'has_model_dropdown':True, 'icon':'fa fa-building', 'models':[
            {'title':'Product Category', 'url':'categories/category/', 'is_active':True},
            {'title':'Product SubCategory', 'url':'categories/subcategories/', 'is_active':True},
            {'title':'Product Type', 'url':'categories/subcategories/', 'is_active':True},
            {'title':'Delivery Fee', 'url':'payments/deliveryfeecalculator/', 'is_active':True},
            # {'title':'Email Templates', 'url':'system_settings/emailtemplates/', 'is_active':True},
        ],
    },
]