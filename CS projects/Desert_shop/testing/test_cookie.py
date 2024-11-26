from desert import cookie
def test_cookie():
    tstcnd=cookie("sugar",3,1)
    assert tstcnd.gt_nm()==tstcnd.nm
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan
    assert tstcnd.calctx()==round(tstcnd.cost()*tstcnd.txp*100)/100
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_