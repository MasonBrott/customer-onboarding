project_id = "cmmcmsp-prod"
env        = "prod"

jump_server_vm_name = "jump-server"

realms = {
  0 : {
    name : "Realm1"
    regions : ["us-central1"]
    customers : {
      "ATXDefense" : {
        domain : "test1.cmmc.space",
      }
      "SKS" : {
        domain : "test2.cmmc.space",
      }
      "ATX Prod" : {
        domain : "test3.cmmc.space",
      }
      "GS" : {
        domain : "test4.cmmc.space"
      }
    }
  }
}