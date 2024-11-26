from desert import sunday
def test_sunday():
    tstcnd=sunday("vanil sprink",2,1,"sprink",1)
    assert tstcnd.gt_nm()==tstcnd.nm
    # assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan
    assert tstcnd.calctx()==round(tstcnd.cost()*tstcnd.txp*100)/100
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_+tstcnd.ppt
