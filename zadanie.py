http://127.0.0.1:5000/oblicz?l1=10&l2=20&op=plus
@app.route('/oblicz')
def oblicz():
    l1_arg = request.args.get('l1')
    if l1_arg is None:
        return 'brak argumentu l1'
    l1 = int(l1_arg)
    
    l2_arg = request.args.get('l2')
    if l2_arg is None:
        return 'brak argumentu l2'
    l2 = int(l2_arg)
    
    op = request.args.get('op')
    
    if op == 'plus':
        s = l1 + l2
        return f'{s}'
        
    if op == 'dzielenie':
        d = l1 / l2
        return f'{d}'
        
    if op == 'odejmowanie':
        o = l1 - l2 
        return f'{o}'
        
    if op == 'mnożenie':
        m = l1 * l2
        return f'{m}'
        
        return ""
    
        
