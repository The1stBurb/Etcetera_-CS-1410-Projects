from desert import sunday
def test_sunday():
    tstcnd=sunday("vanil sprink",2,1,"sprink")
    assert tstcnd.gt_nm()==tstcnd.nm
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan
    assert tstcnd.calctx()==tstcnd.cost()*tstcnd.txp
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_+tstcnd.ppt
