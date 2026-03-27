.global _start
.text
_start:

 // - Numero: 15.5 - 
 ldr r0, =num_1 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 4.5 - 
 ldr r0, =num_2 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: + - 
 vpop {d0} 
 vpop {d1} 
 vadd.f64 d2, d1, d0 
 // - Numero: 20.0 - 
 ldr r0, =num_3 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 5.0 - 
 ldr r0, =num_4 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: - - 
 vpop {d0} 
 vpop {d1} 
 vsub.f64 d2, d1, d0 
 // - Numero: 3.0 - 
 ldr r0, =num_5 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 4.0 - 
 ldr r0, =num_6 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: * - 
 vpop {d0} 
 vpop {d1} 
 vmul.f64 d2, d1, d0 
 // - Numero: 10.0 - 
 ldr r0, =num_7 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 2.0 - 
 ldr r0, =num_8 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: / - 
 vpop {d0} 
 vpop {d1} 
 vdiv.f64 d2, d1, d0 
 // - Numero: 10.0 - 
 ldr r0, =num_9 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 3.0 - 
 ldr r0, =num_10 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: // - 
 vpop {d0} 
 vpop {d1} 
 vdiv.f64 d2, d1, d0 
 vcvt.s32.f64 s0, d2 
 vcvt.f64.s32 d2, s0 
 // - Numero: 10.0 - 
 ldr r0, =num_11 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 3.0 - 
 ldr r0, =num_12 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: % - 
 vpop {d0} 
 vpop {d1} 
 vdiv.f64 d2, d1, d0 
 vcvt.s32.f64 s0, d2 
 vcvt.f64.s32 d2, s0 
 vmul.f64 d2, d2, d0 
 vsub.f64 d2, d1, d2 
 // - Numero: 2.0 - 
 ldr r0, =num_13 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 3.0 - 
 ldr r0, =num_14 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: ^ - 
 vpop {d0} 
 vpop {d1} 
 vcvt.s32.f64 s0, d0 
 vmov r2, s0 
 ldr r0, =num_15 
  vldr d2, [r0] 

ciclo_potencia_1:
 cmp r2, #0 
 ble fim_potencia_1 
 vmul.f64 d2, d2, d1 
 sub r2, r2, #1 
 b ciclo_potencia_1 

fim_potencia_1:
 vpush {d2} 

 // - Numero: 5.0 - 
 ldr r0, =num_16 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 2.0 - 
 ldr r0, =num_17 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: * - 
 vpop {d0} 
 vpop {d1} 
 vmul.f64 d2, d1, d0 
 // - Numero: 3.0 - 
 ldr r0, =num_18 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: + - 
 vpop {d0} 
 vpop {d1} 
 vadd.f64 d2, d1, d0 
 // - Numero: 10.0 - 
 ldr r0, =num_19 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 2.0 - 
 ldr r0, =num_20 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: / - 
 vpop {d0} 
 vpop {d1} 
 vdiv.f64 d2, d1, d0 
 // - Numero: 3.0 - 
 ldr r0, =num_21 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 1.0 - 
 ldr r0, =num_22 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: + - 
 vpop {d0} 
 vpop {d1} 
 vadd.f64 d2, d1, d0 
 // - Operador: * - 
 vpop {d0} 
 vpop {d1} 
 vmul.f64 d2, d1, d0 
 // - Numero: 100.0 - 
 ldr r0, =num_23 
 vldr d0, [r0] 
 vpush {d0} 

 // - Numero: 10.0 - 
 ldr r0, =num_24 
 vldr d0, [r0] 
 vpush {d0} 

 // - Operador: / - 
 vpop {d0} 
 vpop {d1} 
 vdiv.f64 d2, d1, d0 

_fim:
 b _fim 

.data
num_1: .double 15.5
num_2: .double 4.5
num_3: .double 20.0
num_4: .double 5.0
num_5: .double 3.0
num_6: .double 4.0
num_7: .double 10.0
num_8: .double 2.0
num_9: .double 10.0
num_10: .double 3.0
num_11: .double 10.0
num_12: .double 3.0
num_13: .double 2.0
num_14: .double 3.0
num_15: .double 1.0
num_16: .double 5.0
num_17: .double 2.0
num_18: .double 3.0
num_19: .double 10.0
num_20: .double 2.0
num_21: .double 3.0
num_22: .double 1.0
num_23: .double 100.0
num_24: .double 10.0

variavel_mem: .space 8 
historico_res: .space 800 
ponteiro_res: .word 0 
