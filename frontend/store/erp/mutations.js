export default {
  SET_ERPS(state, erps) {
    state.erps = erps;
  },
  PUT_ERP(state, erpEdit) {
    state.erpEdit = erpEdit;
  },
  SET_ERP_UPDATE(state, erpEdit) {
    state.erpEdit = Object.assign({}, state.erpEdit, erpEdit);
  },
};
