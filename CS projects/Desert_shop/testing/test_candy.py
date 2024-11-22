from desert import candy
def test_candy():
    tstcnd=candy("sugar",5,1)
    assert tstcnd.gt_nm()==tstcnd.nm
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan
    assert tstcnd.calctx()==tstcnd.cost()*tstcnd.txp
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_