import sympy
x,y,z = sympy.symbols('x,y,z')
test= {
    'one_order':
        {
            'parametrs_class_object':{
                'step':0.1,
                'section': [0,0.5]
            },
            'parametrs_for_solve':{
                'func_dict': {
                    y:(y+x)**2
                },
                'sdata_dict':{
                    x:0,
                    y:0
                },
                'ans_vars':(x,y)
            },
            'result_last_depend': {
                'eem': {
                    x:0.5,
                    y:0.031513228
                },
                'ecm':{
                    x:0.5,
                    y:0.047024301
                },
                'iem':{
                    x:0.5,
                    y:0.045387432
                },
                'rkm':{
                  x:0.5,
                  y:0.04630231
                },
                'am':{
                x: 1,
                y: 0.551159854
                },
                'abmm':{
                x: 1,
                y: 0.557625580
                }
            }
        },
    'two_order':{
        'parametrs_class_object': {
            'step': 0.2,
            'section': [0, 1]
        },
        'parametrs_for_solve': {
            'func_dict': {
                y: z,
                z: 2*x*z/(x**2+1)
            },
            'sdata_dict': {
                x: 0,
                y: 1,
                z:3
            },
            'ans_vars': (x, y)
        },
        'result_last_depend':{
            'rkm':{
                x:1.000000 ,
                y:4.99995799
            }
        }
    }
}